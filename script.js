
function checkPasswordSystem() {
  const isEnabled = localStorage.getItem("password_enabled") === "true";
  if (isEnabled) {
    document.getElementById("loginBox").style.display = "block";
  } else {
    document.getElementById("mainContent").style.display = "block";
  }
}

checkPasswordSystem();

function login(event) {
  event.preventDefault();
  const pass = document.getElementById("password").value;
  if (pass === "xgsammim123") {
    document.getElementById("loginBox").style.display = "none";
    document.getElementById("mainContent").style.display = "block";
  } else {
    alert("Invalid password!");
  }
}

async function downloadVideo() {
  const url = document.getElementById("videoUrl").value;
  if (!url) return alert("Please insert a TikTok link.");

  try {
    const response = await fetch(`https://tikwm.com/api/?url=${encodeURIComponent(url)}`);
    const data = await response.json();
    if (data.data && data.data.play) {
      window.open(data.data.play, '_blank');
    } else {
      alert("Download failed. Please try another link.");
    }
  } catch (err) {
    alert("Something went wrong. Please try again later.");
  }
}

function pasteText() {
  navigator.clipboard.readText().then(text => {
    document.getElementById("videoUrl").value = text;
  }).catch(() => {
    alert("Clipboard access denied. Please paste manually.");
  });
}
