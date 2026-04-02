let sessionId = null;

async function send() {
  const query = document.getElementById("q").value;

  const res = await fetch("http://localhost:8000/query", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({query})
  });

  const data = await res.json();
  sessionId = data.session_id;

  document.getElementById("out").innerText =
    JSON.stringify(data, null, 2);
}

async function approve() {
  const res = await fetch("http://localhost:8000/approve", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({session_id: sessionId})
  });

  const data = await res.json();
  document.getElementById("out").innerText =
    JSON.stringify(data, null, 2);
}