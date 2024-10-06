<script>
  import { push } from "svelte-spa-router"; 

  export let toggleSidebar;

  let isMenuOpen = false;

  function toggleMenu() {
    isMenuOpen = !isMenuOpen;
  }

  function navigateTo(route) {
    push(route);
    isMenuOpen = false; 
  }
</script>

<nav class="topbar">
  <div class="logo">
    <img src="./img/JABOTRON.png" alt="Logo" class="logo-img" />
  </div>

  <button class="menu-toggle" on:click={toggleMenu}>
    <i class="bi bi-list"></i>
  </button>

  <div class="menu-container" class:open={isMenuOpen}>
    <ul class="menu">
      <li><a href="/" on:click|preventDefault={() => navigateTo('/')}>Dashboard</a></li> 
      <li><a href="/analise" on:click|preventDefault={() => navigateTo('/analise')}>Analises</a></li>
      <li><a href="/relatorio" on:click|preventDefault={() => navigateTo('/relatorio')}>Relatórios</a></li>
      <li><a href="/sobre" on:click|preventDefault={() => navigateTo('/sobre')}>Sobre nós</a></li>
    </ul>
  </div>

  <button class="sidebar-toggle" on:click={toggleSidebar}>
    <i class="bi bi-layout-sidebar-reverse"></i>
  </button>
</nav>

<style>
  .topbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #FCFCF9;
    padding: 0 1rem;
    border-bottom: 1px solid #ddd;
    position: fixed;
    top: 0;
    right: 0;
    left: 0;
    height: 80px;
    z-index: 100;
  }

  .logo {
    display: flex;
    align-items: center;
  }

  .logo-img {
    width: 220px;
    height: auto;
  }

  .menu-container {
    flex-grow: 1;
  }

  .menu {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin: 0;
    padding: 0;
    justify-content: center;
  }

  .menu li a {
    text-decoration: none;
    color: inherit;
    cursor: pointer;
  }

  .menu li {
    font-size: 1rem;
    color: #666;
    padding: 0.5rem 1rem;
  }

  .menu li:hover {
    color: #000;
  }

  .menu-toggle, .sidebar-toggle {
    display: none;
    background: none;
    border: none;
    font-size: 1.5rem;
    cursor: pointer;
    padding: 0.5rem;
  }

  @media (max-width: 768px) {
    .menu-toggle, .sidebar-toggle {
      display: block;
    }

    .menu-container {
      position: absolute;
      top: 80px;
      left: 0;
      right: 0;
      background-color: #FCFCF9;
      border-bottom: 1px solid #ddd;
      transform: translateY(-100%);
      transition: transform 0.3s ease;
      visibility: hidden;
    }

    .menu-container.open {
      transform: translateY(0);
      visibility: visible;
    }

    .menu {
      flex-direction: column;
      align-items: center;
      padding: 1rem 0;
      gap: 1rem;
      justify-content: center;
      margin: 0;
    }

    .logo-img {
      width: 120px;
    }
  }
</style>
