import { defineStore } from 'pinia';

export const useUserStore = defineStore('userStore', {
  state: () => ({
    isLogin: false,
  }),

  getters: {
    getLoginState(state) {
      return state.isLogin;
    },
  },

  actions: {
    onLogin() {
      this.isLogin = true;
    },
    onLogout() {
      this.isLogin = false;
    },
  },
});
