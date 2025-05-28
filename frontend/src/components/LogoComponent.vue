<template>
    <div class="logo-container" @click="animateLogo">
      <img src="/logo2.jpg" alt="Logo" class="logo" :class="{ 'rotate': isRotating, 'fade': isFading }">
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        isRotating: false,
        isFading: false
      };
    },
    methods: {
      animateLogo() {
        this.isRotating = true;
        setTimeout(() => {
          this.isRotating = false;
          this.isFading = true;
        }, 500);
      }
    }
  };
  </script>
  
  <style>
  .logo-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
  
  .logo {
    width: 100px;
    height: 100px;
    transition: transform 0.5s, opacity 0.5s;
  }
  
  .rotate {
    transform: rotate(360deg);
  }
  
  .fade {
    opacity: 0;
  }
  </style>
  