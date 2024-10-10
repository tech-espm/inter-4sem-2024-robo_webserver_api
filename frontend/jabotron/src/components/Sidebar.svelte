<script>
    export let isOpen = false;
    export let toggleSidebar;
</script>
  
<button class="sidebar-overlay" class:active={isOpen} on:click={toggleSidebar}></button>
<div class="sidebar" class:active={isOpen}>
    <div class="sidebar-header">
      <div class="icons">
        <i class="bi bi-search" />
        <i class="bi bi-chat" />
        <i class="bi bi-bell" />
      </div>
      <img src="https://via.placeholder.com/50" alt="Profile" class="profile-picture" />
    </div>
  
    <div class="sidebar-foto">
      <img src="./img/fazenda.png" alt="Logo" class="farm-img" />
    </div>
  
    <div class="sidebar-footer">
      <i class="bi bi-box-arrow-left" />
    </div>
</div>
  
<style>
    .sidebar-overlay {
      display: none;
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(0, 0, 0, 0.5);
      z-index: 900;
    }
  
    .sidebar {
      width: 270px;
      height: 100vh;
      background-color: #334D40;
      position: fixed;
      top: 0;
      right: 0;
      padding: 20px;
      color: white;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      z-index: 1000;
      transition: transform 0.3s ease;
    }
  
    @media (max-width: 768px) {
      .sidebar {
        width: 200px; 
        transform: translateX(100%);
        height: 100vh;
      }
  
      .sidebar.active {
        transform: translateX(0);
      }
  
      .sidebar-overlay {
        display: block;
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.3s ease;
      }
  
      .sidebar-overlay.active {
        opacity: 1;
        pointer-events: auto;
      }

      .icons :global(i) {
        margin-right: 10px; 
      }

      .farm-img {
        width: 200px;
      }
    }
  
    .sidebar-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 5px;
    }
  
    .icons {
      display: flex;
    }
  
    .icons :global(i) {
      margin-right: 30px;
    }
  
    .profile-picture {
      width: 50px;
      height: 50px;
      border-radius: 50%;
    }
  
    .sidebar-foto {
      margin-top: 20px;
      width: 100%;
      height: auto;
      display: flex;
      justify-content: center;
      margin-bottom: 50px;
    }
  
    .farm-img {
      max-width: 270px;
      height: auto;
      opacity: 20%;
      filter: invert(100%);
    }
  
    .sidebar-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px 0;
    }
</style>