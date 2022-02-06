
// get the current url of the page the user is on
chrome?.tabs?.query({ active: true }, function (tabs) {
  const urlStrings = tabs[0].url.split("/");
  if (urlStrings.some(str => str.includes('twitch.tv'))) {
    submit(urlStrings[urlStrings.length - 1])
  }
});

//
let tmiClient;
let socket;
let sentiment = ".50";

const startAnalyzingButton = document.querySelector("#start-analyze");
const channelNameInput = document.querySelector("#channel-input");
const numberMessagesInput = document.getElementById("number-messages-input");

const mainScreen = document.querySelector(".title-screen");
const analysisTab = document.querySelector(".analysis-tab");

channelNameInput.addEventListener("keydown", (e) => {
  if (e.key == "Enter") {
    submit(channelNameInput.value);
  }
});

startAnalyzingButton.addEventListener("click", (e) => {
  submit(channelNameInput.value);
});

function submit(channelName) {
  tmiClient = new tmi.Client({
    connection: {
      secure: true,
      reconnnect: true,
    },
    channels: [channelName],
  });

  mainScreen.style.display = 'none';
  analysisTab.style.display = 'block';

  tmiClient.connect().then(() => {
    console.log(`Listening for messages in ${channelName}...`);
  });

  socket = io("http://127.0.0.1:5000/");

  socket.on("connect", () => {
    socket.emit("connection", {
      streamer: channelName,
      numMessages: 10,
    });
    tmiClient.on("message", (channel, tags, message, self) => {
      socket.emit("message", { msg: `${tags["display-name"]}: ${message}` });
    });
  });

  // data is now an int
  socket.on("percentage-update", (data) => {
    // update the percentage itself displayed
    var r = document.querySelector(":root");
    var percentString = String(data);
    r.style.setProperty("--percent", percentString);
    document.getElementById("percentage").innerHTML = percentString;

    // update the progress pie circle
    const progressBar = document.querySelector('div[role="progressbar"]');
    progressBar.style.setProperty("--value", data);

    // update the background color
    updateBackground(data);
  });

  socket.on("test-event", (data) => {
    console.log(data);
  })

  // update the channel name in analysis page
  const capChannel = channelName.charAt(0).toUpperCase() + channelName.slice(1);
  document.getElementById("channel").textContent = capChannel;
}

function returnNumComments() {
  let inputVal = document.getElementById("number-messages-input").value;
  socket.emit("changeNumMessages", { numMessages: inputVal });
  console.log(`numcomment: ${inputVal}!`);
}

function createRadialGradient() {
  var c = document.getElementById("newCanvas");
  var ctxt = c.getContext("2d");
  var linegrd = ctxt.createRadialGradient(75, 50, 5, 90, 60, 100);
  linegrd.addColorStop(0, "#FFFFFF");
  linegrd.addColorStop(1, "#66CC00");
  ctxt.fillStyle = linegrd;
  ctxt.fillRect(20, 10, 200, 150);
}

function getSentiment() {
  return sentiment;
}

// takes in a percent between 0 and 100
function updateBackground(number) {
  var hue = hue = Math.floor((number)/100 * 120);;
  if (hue < 80){
    hue = Math.floor((number)/400 * 120);
  }
  var saturation = (Math.abs(number - 50) / 50 )*100; // fade to white as it approaches 50
  var alpha = 100;
  document.body.style.backgroundColor = `hsla(${hue},${saturation}%,100%,${alpha}%)`;
  // console.log(`hsl(${hue},${saturation}%,${light}%)`);
}

function updateBackground2(number) {
  if (number < 50) {
    let num = ((number - 50)/50)*100;
    console.log(num)
    document.body.style.backgroundColor = `hsla(0, 100%, 50%, ${num}%)`
  } else {
    let num = ((50 - number)/50)*100;
    console.log(num)
    document.body.style.backgroundColor = `hsla(120, 100%, 50%, ${num}%)`
  }
}