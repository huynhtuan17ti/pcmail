// find the body of the content
export function findMessage(content) {
  var message = 'No data found!';
  if ('data' in content.body) {
    var encodedBody = content.body.data;
    message = atob(encodedBody); // decoder
  } else if ('data' in content.parts[0].body) {
    var encodedBody = content.parts[0].body.data;
    var encodedBody = encodedBody
      .replace(/-/g, '+')
      .replace(/_/g, '/')
      .replace(/\s/g, '');
    //console.log(encodedBody);
    message = atob(encodedBody); // decoder
    message = message.split('\n')[0]; // only return the first message
  }
  return message;
}

export function findAttachmentId(content) {
  var id = undefined;
  if ('attachmentId' in content.body) {
    id = content.body.attachmentId;
  } else {
    for (var partId = 0; partId <= 1; partId++) {
      if ('attachmentId' in content.parts[partId].body) {
        id = content.parts[partId].body.attachmentId;
        break;
      }
    }
  }
  return id;
}

export function findMessageId(content) {
  return content.id;
}
