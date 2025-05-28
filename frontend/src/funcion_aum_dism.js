import { createApp } from 'vue';
import App from './App.vue';
import $ from 'jquery';


$(document).ready(function() {
  console.log('jQuery is ready!');
  $('body').css('background-color', '#f0f0f0');
});

createApp(App).mount('#app');