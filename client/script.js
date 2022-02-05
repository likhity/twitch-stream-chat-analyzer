// var aWebSocket = new WebSocket("http://127.0.0.1:5000/", [])

//changing screens
const tabs = document.querySelectorAll('[data-tab-target');
const tabContents = document.querySelectorAll('[data-tab-content');

tabs.forEach(tab => {
  tab.addEventListener('click', ()=> {
    const target = document.querySelector(tab.dataset.tabTarget);
    tabContents.forEach(tabContent =>{
      tabContent.classList.remove('active');
    });
    tabs.forEach(tab =>{
      tab.classList.remove('active');
    });
    tab.classList.add('active');
    target.classList.add('active');
  });
});

// get the current url of the page the user is on
chrome.tabs.query({active:true},function(tab){
  url = tab.url;
});

//
let tmiClient;
let socket;

const startAnalyzingButton = document.querySelector("#start-analyze");
const channelNameInput = document.querySelector("#channel-input");
const numberMessagesInput = document.getElementById("number-messages-input");


channelNameInput.addEventListener('keydown', (e) => {
  if (e.key == 'Enter') {
    submit(channelNameInput.value);
  }
})

startAnalyzingButton.addEventListener('click', (e) => {
    submit(channelNameInput.value);
})

function submit(channelName) {
  tmiClient = new tmi.Client({
    connection: {
      secure: true,
      reconnnect: true,
    },
    channels: [channelName]
  })
  
  tmiClient.connect().then(() => {
    console.log(`Listening for messages in ${channelName}...`);
  });

  socket = io("http://127.0.0.1:5000/");

  socket.on("connect", () => {
    socket.emit("connection", { user: channelName, numMessages: parseInt(numberMessagesInput.value) });
    tmiClient.on('message', (channel, tags, message, self) => {
      socket.emit("message", { msg: `${tags['display-name']}: ${message}`})
    })
  })
  
}

// set number of comments in the bootstrap dropdown menu to the right
function setNumComments() {  
  var mylist = document.getElementById("Dropdown button");  
  document.getElementById("favourite").value = mylist.options[mylist.selectedIndex].text;  
  }

function createRadialGradient(){
  var c = document.getElementById("newCanvas");
  var ctxt = c.getContext("2d");
  var linegrd = ctxt.createRadialGradient(75, 50, 5, 90, 60, 100);
  linegrd.addColorStop(0, "#FFFFFF");
  linegrd.addColorStop(1, "#66CC00");
  ctxt.fillStyle = linegrd;
  ctxt.fillRect(20, 10, 200, 150);
}