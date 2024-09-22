<script>
    import Sidebar from './components/Sidebar.svelte';
    import Header from './components/Header.svelte';
    import SoilAnalysis from './components/SoilAnalysis.svelte';
    import NutrientsLevels from './components/NutrientsLevels.svelte';
  </script>
  
  <div class="app">
    <Sidebar />
    <div class="main-content">
      <Header />
      <div class="dashboard">
        <SoilAnalysis />
        <NutrientsLevels />
      </div>
    </div>
  </div>
  
  <style>
    .app {
      display: flex;
      height: 100vh;
      width: 100%;
    }
  
    .main-content {
      flex: 1;
      background-color: #f6f7f9;
      padding: 2rem;
      margin-left: 250px; /* Ajustando margem para sidebar */
    }
  
    .dashboard {
      display: flex;
      flex-direction: column; /* Nutrients Levels agora vai ficar abaixo do Soil Analysis */
      gap: 2rem;
    }
  </style>
  