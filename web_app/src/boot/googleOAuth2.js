import { boot } from 'quasar/wrappers';
import VueGapi from 'vue-gapi';
import { API_KEY, CLIENT_ID, DISCOVERY_DOCS, SCOPE } from 'src/constants/gapi';
//import GAuth from 'vue3-google-oauth2';
const gauthOption = {
  apiKey: API_KEY,
  clientId: CLIENT_ID,
  discoveryDocs: DISCOVERY_DOCS,
  scope: SCOPE,
  prompt: 'consent',
  // https://stackoverflow.com/a/72197117
  plugin_name: 'pcmail',
  fetch_basic_profile: true,
};

export default boot(({ app }) => {
  app.use(VueGapi, gauthOption);
});
