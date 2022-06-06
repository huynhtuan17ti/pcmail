export async function sendMessage(Gapi, headers_obj, message) {
  var sentData = undefined;
  var email = '';
  for (var header in headers_obj)
    email += header += ': ' + headers_obj[header] + '\r\n';

  email += '\r\n' + message;
  await Gapi.getGapiClient().then(async (gapi) => {
    await gapi.client.gmail.users.messages
      .send({
        userId: 'me',
        resource: {
          raw: btoa(email).replace(/\+/g, '-').replace(/\//g, '_'),
        },
      })
      .then(async () => {
        sentData = await getMessageData(Gapi);
      });
  });

  return sentData;
}

export async function getMessageData(Gapi, filter) {
  var data = undefined;
  await Gapi.getGapiClient().then(async (gapi) => {
    await gapi.client.gmail.users.messages
      .list({
        maxResults: 1,
        userId: 'me',
        format: 'full',
        q: filter,
      })
      .then(async (response) => {
        try {
          var message = response.result.messages[0];
          //console.log(message.id);
          await gapi.client.gmail.users.messages
            .get({
              userId: 'me',
              id: message.id,
              format: 'full',
            })
            .then((mail) => {
              data = mail.result;
            });
        } catch (err) {}
      });
  });
  return data;
}

export const getSentMessage = async (Gapi) => {
  return await getMessageData(Gapi, 'in:sent');
};

export const getThreadLastMessage = async (Gapi, threadID) => {
  var lastMessageData = undefined;
  await Gapi.getGapiClient().then(async (gapi) => {
    await gapi.client.gmail.users.threads
      .get({
        userId: 'me',
        id: threadID,
      })
      .then(async (response) => {
        //console.log(response);
        var messages = response.result.messages;
        if (messages.length >= 2) {
          lastMessageData = messages[1];
        }
      });
  });
  return lastMessageData;
};

export const waitResponse = async (Gapi, threadID) => {
  var time = 0;
  return await new Promise((resolve) => {
    const interval = setInterval(async () => {
      var response = await getThreadLastMessage(Gapi, threadID);
      console.log(time + ': ' + response);
      time += 1;
      if (time == 30) {
        return undefined;
      }
      if (response !== undefined) {
        resolve(response);
        clearInterval(interval);
        console.log('Done!');
      }
    }, 3000);
  });
};
