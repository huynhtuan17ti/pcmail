import { boot } from 'quasar/wrappers';
import VueGapi from 'vue-gapi';
//import GAuth from 'vue3-google-oauth2';
const gauthOption = {
  apiKey: 'AIzaSyAmmrXQL9VJWfEuB_Fc8DWIcfTfV0SN_6o',
  clientId:
    '67393825355-aseggp161v49soh8vo33d7gq5dltpaie.apps.googleusercontent.com',
  discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/gmail/v1/rest'],
  scope:
    'https://www.googleapis.com/auth/gmail.send https://www.googleapis.com/auth/gmail.readonly',
  prompt: 'consent',
  // https://stackoverflow.com/a/72197117
  plugin_name: 'pcmail',
  fetch_basic_profile: true,
};

export default boot(({ app }) => {
  app.use(VueGapi, gauthOption);
});
