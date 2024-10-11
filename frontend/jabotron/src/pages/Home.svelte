<script>
    import SoloAnalise from '../components/SoloAnalise.svelte';
    import Tempo from '../components/Tempo.svelte';
    import Umidade from '../components/Umidade.svelte';
    import Radar from '../components/Radar.svelte';
  </script>
  
  <h1 class="bemv">Bem-Vindo de volta, Luca!</h1>
  <div class="row">
    <div class="col-md-4">
      <Tempo />
    </div>
    <div class="col-md-8">
      <SoloAnalise />
    </div>
  </div>
  <div class="row">
    <div class="col-md-4">
        <Umidade/>
    </div>
    <div class="col-md-4">
      <Radar/>
    </div>

  </div>

  <style>
    .bemv{
        font-size: 24px;
        font-weight: bold;
        color: #2d5a4c;
        margin: 20px;
    }
  </style>