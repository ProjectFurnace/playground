
function handler(event) {
  console.log(JSON.stringify(event));
  let payload = tryParseJSON(event.textPayload);
  let buildId = null;
  if(!payload){
    buildId = event.resource.labels.build_id;
    payload = event.textPayload;
  }else{
    buildId = payload.resource.labels.build_id;
    payload = payload.textPayload;
  }
  const parsedEvent = {};
  parsedEvent.build_id = buildId;
  parsedEvent.message = payload;
  parsedEvent.timestamp = event.receiveTimestamp;
  parsedEvent.Id = new Date().getTime().toString();
  console.log(parsedEvent);
  return parsedEvent;
}

function tryParseJSON (jsonString){
  try {
      var o = JSON.parse(jsonString);

      // Handle non-exception-throwing cases:
      // Neither JSON.parse(false) or JSON.parse(1234) throw errors, hence the type-checking,
      // but... JSON.parse(null) returns null, and typeof null === "object", 
      // so we must check for that, too. Thankfully, null is falsey, so this suffices:
      if (o && typeof o === "object") {
          return o;
      }
  }
  catch (e) { }

  return null;
}


function setup() {
}

module.exports.handler = handler;
module.exports.setup = setup;