import { defineStore } from 'pinia';

export const useUserStore = defineStore('userStore', {
  state: () => ({
    isLogin: !!localStorage.getItem('token'),
  }),

  getters: {
    getLoginState(state) {
      return state.isLogin;
    },
  },

  actions: {
    onLogin() {
      this.isLogin = true;
      localStorage.setItem('token', 'JWT');
    },
    onLogout() {
      this.isLogin = false;
      localStorage.removeItem('token');
    },
  },
});
