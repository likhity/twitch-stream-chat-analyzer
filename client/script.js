
// get the current url of the page the user is on
chrome?.tabs?.query({ active: true }, function (tabs) {
  console.log(tabs);
  const tabUrls = tabs.map(tab => tab.url);
  console.log(tabUrls);
  const urlStrings = tabUrls.find(tabUrl => {
    return tabUrl?.match("twitch.tv") != null
  }).split("/");
  if (urlStrings.some(str => str.includes('twitch.tv'))) {
    if ((urlStrings[urlStrings.length - 1] !== '')) {
      submit(urlStrings[urlStrings.length - 1])
    }
  }
});


let tmiClient;
let socket;
let sentiment = "50";

var startAnalyzingButton = document.querySelector("#start-analyze");
var channelNameInput = document.querySelector("#channel-input");

var mainScreen = document.querySelector(".title-screen");
var analysisTab = document.querySelector(".analysis-tab");

  


socket = io("http://127.0.0.1:5000/");

channelNameInput.addEventListener("keydown", (e) => {
  if (e.key == "Enter") {
    submit(channelNameInput.value);
  }
});

startAnalyzingButton.addEventListener("click", (e) => {
  submit(channelNameInput.value);
});

function submit(channelName) {
  updateBackground();
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
    document.getElementById("num-messages").value = 10;
    document.getElementById("num-messages").addEventListener("change", (e) => {
      var num = document.getElementById("num-messages").value;
      console.log(num);
      socket.emit("changeNumMessages", {
        numMessages: num,
      });
    });
  });


  socket.on("connect", () => {
    socket.emit("connection", {
      user: channelName,
      numMessages: 10,
    });
    tmiClient.on("message", (channel, tags, message, self) => {
      socket.emit("message", { msg: `${tags["display-name"]}: ${message}`, streamer: channelName });
    });
    updateBackground(sentiment);
  });

  // data is now an int
  socket.on("percentage-update", (data) => {
    sentiment = data;
    // update the percentage itself displayed
    var r = document.querySelector(":root");
    var percentString = String(data);
    r.style.setProperty("--percent", percentString);
    document.getElementById("percentage").innerHTML = percentString;

    animateCircle();
    // update the background color
    updateBackground();

    setTimeout(() => {
      if (document.getElementById("percentage").textContent.trim() === '50') {
        document.getElementById("streaming-alert").classList.remove("d-none");
        document.getElementById("streaming-alert").querySelector("button").addEventListener("click", () => {
          document.getElementById("streaming-alert").remove()
        })
      }
    }, 10000)
  });

  // update the channel name in analysis page
  const capChannel = channelName.charAt(0).toUpperCase() + channelName.slice(1);

  // initialize analysis page elements too
  document.getElementById("channel").textContent = capChannel;
}

function returnNumComments() {
  let inputVal = document.getElementById("dropdownMenuButton").value;
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

// takes in a percent between 0 and 100
function updateBackground() {
  var hue = Math.floor((sentiment)/100 * 120);;
  // var saturation = (Math.abs(number - 50) / 50 )*100; // fade to white as it approaches 50
  var saturation = 100;
  var lightness = 70;
  var alpha = 0.5;
  
  // document.body.style.backgroundColor = "yellow";
  // document.body.style.backgroundColor = `hsla(${hue},${saturation}%,${lightness}%,${alpha})`;
  var color = `hsla(${hue},${saturation}%,${lightness}%,${alpha})`;
  var lightcolor = `hsla(${hue},${saturation}%,90%,${alpha})`;
  // document.body.style.backgroundColor = color;
  document.body.style = `background-image : radial-gradient(${color},${lightcolor});`;
  // console.log(`hsl(${hue},${saturation}%,${alpha}%)`);

}
function animateCircle(){
  // var progressBar = document.querySelector('div[role="progressbar"]');
  // var curr = progressBar.style.value;
  // console.log(curr);

  // document.documentElement.style.setProperty('--first-degree', curr);
  // document.documentElement.style.setProperty('--second-degree', sentiment);

  // progressBar.style.animation= "turn";
  progressBar.style.setProperty("--value", sentiment);
}
