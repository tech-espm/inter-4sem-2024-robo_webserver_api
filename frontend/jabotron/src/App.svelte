<!-- App.svelte -->
<script>
  import Sidebar from './components/Sidebar.svelte';
  import Topbar from './components/Topbar.svelte';
  import Tempo from './components/Tempo.svelte';
  import SoloAnalise from './components/SoloAnalise.svelte';

  let activeTab = 'dashboard';
  let isSidebarOpen = false;

  function handleTabChange(tab) {
    activeTab = tab;
  }

  function toggleSidebar() {
    isSidebarOpen = !isSidebarOpen;
  }
</script>

<div class="app-container">
  <div class="main-content">
    <Topbar {activeTab} {toggleSidebar} on:tabChange={handleTabChange} />

    <div class="content">
      <div class="row">
        <div class="col-md-6">
          <Tempo/>
        </div>
        <div class="col-md-6">
          <SoloAnalise/>
        </div>
      </div>
    </div>
  </div>
  <Sidebar isOpen={isSidebarOpen} {toggleSidebar}/>
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

  .content {
    padding: 20px;
  }
</style>