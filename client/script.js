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
let client;
let socket;

const startAnalyzingButton = document.getElementById("start-analyze");
const channelNameInput = document.getElementById("channel-input");


channelNameInput.addEventListener('keydown', (e) => {
  if (e.key == 'Enter') {
    submit(channelNameInput.value);
  }
})

startAnalyzingButton.addEventListener('click', (e) => {
    submit(channelNameInput.value);
})

function submit(channelName) {
  client = new tmi.Client({
    connection: {
      secure: true,
      reconnnect: true,
    },
    channels: [channelName]
  })
  
  client.connect().then(() => {
    console.log(`Listening for messages in ${channelName}...`);
  });

  socket = io("http://127.0.0.1:5000/");

  socket.on("connect", () => {
    socket.emit("my event", { data: "Im connected" });
  })
  
  client.on('message', (channel, tags, message, self) => {
    console.log(`${tags['display-name']}: ${message}`)
  })
}

