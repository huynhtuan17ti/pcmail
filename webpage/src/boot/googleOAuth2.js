import { boot } from 'quasar/wrappers';
import GAuth from 'vue3-google-oauth2';
const gauthOption = {
  clientId:
    '67393825355-aseggp161v49soh8vo33d7gq5dltpaie.apps.googleusercontent.com',
  scope: 'profile email',
  prompt: 'consent',
  // https://stackoverflow.com/a/72197117
  plugin_name: 'pcmail',
  fetch_basic_profile: true,
};

export default boot(({ app }) => {
  app.use(GAuth, gauthOption);
});
