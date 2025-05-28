<template>
  <div class="content">
    <div class="logo-container" @click="animateLogo">
      <img src="/logo2.jpg" alt="Logo" class="logo" :class="{ 'rotate': isRotating }">
    </div>
    <div class="labels">
      <label class="ctrl-gastos">Control de Gastos</label>
      <label class="est-rdos">Estado de Resultados</label>
    </div>
    <div class="dropdown">
      <label for="titular">Titular del Ingreso o del Gasto:</label>
      <select id="titular" name="titular">
        <option value="" selected>Seleccione el titular</option>
      </select>
    </div>
    <div class="textbox">
      <label for="monto">Monto Gasto:</label>
      <input type="text" id="monto" name="monto">
    </div>
    <div id="montoi" class="textbox" style="position: relative; top: 410px;">
      <label for="montoi">Monto Ingreso:</label>
      <input type="text" id="montoi" name="montoi">
    </div>
    <div class="radio-buttons" style="position: relative; top: -70px;">
      <label for="pesos">Pesos:</label>
      <input type="radio" id="ARS" name="moneda" value="ARS">
      <label for="dolares">Dólares:</label>
      <input type="radio" id="USD" name="moneda" value="USD">
    </div>
    <div class="radio-buttons-i" style="position: relative; top: 400px;">
      <label for="pesos">Pesos:</label>
      <input type="radio" id="ARS" name="moneda" value="ARS">
      <label for="dolares">Dólares:</label>
      <input type="radio" id="USD" name="moneda" value="USD">
    </div>
    <div class="dropdown" style="position: relative; top: -120px;">
  <label for="concepto">Tipo de Gasto:</label>
  <select id="concepto" name="concepto">
    <option value="" selected>Seleccione un concepto</option>
  </select>
</div>
<div class="dropdown" style="position: relative; top: 300px;">
  <label for="concepto2">Tipo de Ingreso:</label>
  <select id="concepto2" name="concepto2">
    <option value="" selected>Seleccione un concepto</option>
  </select>
</div>
<div class="fecha" style="position: relative; top: -200px;">
  <label for="fecha">Fecha del Gasto:</label>
  <input type="date" id="fecha" name="fecha">
</div>
</div>
<div class="fechai" style="position: relative; top: 250px;">
  <label for="fechai">Fecha del Ingreso:</label>
  <input type="date" id="fechai" name="fechai">
</div>

<div class="botonera-gastos">
  <button id="grabarGastoBtn">GRABAR</button>
  <button id="nuevoBtng">NUEVO</button>
</div>
<div class="botonera-ingresos">
  <button id="grabarIngresoBtn">GRABAR</button>
  <button id="nuevoBtni">NUEVO</button>
</div>


</template>

<script>
export default {
  data() {
    return {
      isRotating: false
    };
  },
  methods: {
    animateLogo() {
      this.isRotating = true;
      setTimeout(() => {
        this.isRotating = false;
      }, 500);
    }
  }
};


</script>


