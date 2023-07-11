import './assets/main.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import { createI18n } from 'vue-i18n';
import ru from '@/translate/ru.json';
import en from '@/translate/en.json';

import { createApp } from 'vue';
import { createPinia } from 'pinia';

const i18n = createI18n({
  locale: localStorage.getItem('lang') || 'ru',
  allowComposition: true,
  messages: { ru, en }
});

import App from './App.vue';
import router from './router';

const app = createApp(App);

app.use(i18n);
app.use(createPinia());
app.use(router);

app.mount('#app');
