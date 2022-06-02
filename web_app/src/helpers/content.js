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
    message = message.split('\n')[0]; // just return the first message
  }
  return message;
}
