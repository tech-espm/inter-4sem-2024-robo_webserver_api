<script>
    import SoloAnalise from '../components/SoloAnalise.svelte';
    import Tempo from '../components/Tempo.svelte';
    import Umidade from '../components/Umidade.svelte';
    import Radar from '../components/Radar.svelte';
  </script>
  
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