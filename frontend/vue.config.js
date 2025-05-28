const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  devServer: {
    port: 8081,
    historyApiFallback: false
    
  },
  transpileDependencies: true,
  pages: {
    prueba_each: {
      entry: 'src/prueba_each.js', // Punto de entrada para la nueva página "prueba_each"
      template: 'public/prueba_each.html', // Plantilla HTML para la nueva página "prueba_each"
      filename: 'prueba_each.html' // Nombre del archivo de salida
    },
    funcion_bind: { 
      entry: 'src/funcion_bind.js',         // Punto de entrada para la nueva página "funcion_bind"
      template: 'public/funcion_bind.html', // Plantilla HTML para la nueva página "funcion_bind"
      filename: 'funcion_bind.html'   // Nombre del archivo de salida
    },

                // Punto de entrada aplicación ::::lucymar-app ::::
    Login: {
      entry: 'src/login.js',          // Punto de entrada para la nueva página "login lucymar-app"
      template: 'public/login.html', // Plantilla HTML para la nueva página "login lucymar-app"
      filename: 'login.html'       // Nombre del archivo de salida
    },
    funcion_logo: {
      entry: 'src/pagina_principal.js',     // Punto de entrada para la pagina principal "lucymar-app"
      template: 'public/pagina_principal.html', // Plantilla HTML para la página principal "lucymar-app"
      filename: 'pagina_principal.html'  // Nombre del archivo de salida
    },

    funcion_aum_dism: {

      entry: 'src/funcion_aum_dism.js',     // Punto de entrada para la pagina principal "funcion_aum_dism"
      template: 'public/funcion_aum_dism.html', // Plantilla HTML para la página principal "funcion_aum_dism"
      filename: 'funcion_aum_dism.html'  // Nombre del archivo de salida

    },

    estadistica: {
      entry: 'src/estadistica.js',     // Punto de entrada para la pagina principal "estadistica"
      template: 'public/estadistica.html', // Plantilla HTML para la página principal "estadistica"
      filename: 'estadistica.html'  // Nombre del archivo de salida
    },
  }
})
