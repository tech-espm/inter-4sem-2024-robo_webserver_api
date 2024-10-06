<script>
  import Sidebar from './components/Sidebar.svelte';
  import Topbar from './components/Topbar.svelte';
  import Router from 'svelte-spa-router';  
  import Home from './pages/Home.svelte';  
  import Relatorio from './pages/Relatorio.svelte';
  import Sobre from './pages/Sobre.svelte';
  import Analise from './pages/Analise.svelte';

  let isSidebarOpen = false;

  function toggleSidebar() {
    isSidebarOpen = !isSidebarOpen;
  }

  const routes = {
    '/': Home,  
    '/relatorio': Relatorio,
    '/sobre': Sobre,
    '/analise' : Analise
  };
</script>

<div class="app-container">
  <div class="main-content">
    <Topbar {toggleSidebar} />
    <Router {routes} />
  </div>
  <Sidebar isOpen={isSidebarOpen} {toggleSidebar} />
</div>

<style>
  .app-container {
    display: flex ;
  }

  .main-content {
    flex-grow: 1;
    margin-top: 80px;
  }

  @media (min-width: 769px) {
    .main-content {
      margin-right: 270px;
    }
  
  }
</style>