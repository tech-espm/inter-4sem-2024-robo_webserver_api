<script>
    let autoIrrigation = true;
    let frostProtection = false;
  </script>
  
  <aside class="sidebar">
    <div class="sidebar-header">
      <h2>Jabotron</h2> 
    </div>
  
    <nav class="sidebar-content">
      <h4>Auto scenes</h4>
      <div class="auto-scenes">
        <div class="card">
          <div class="toggle-option auto-irrigation-option">
            <span><i class="fas fa-tint"></i> Auto irrigation</span> 
            <label class="switch">
              <input type="checkbox" checked> 
              <span class="slider round"></span>
            </label>
          </div>
        </div>
  
        <div class="card">
          <div class="toggle-option frost-protection-option">
            <span><i class="fas fa-snowflake"></i> Frost Protection</span> 
            <label class="switch">
              <input type="checkbox"> 
              <span class="slider round"></span>
            </label>
          </div>
        </div>
      </div>
  
      <div class="settings">
        <h4>Settings</h4>
        <div class="settings-grid">
          <div class="card">
            <a href="#"><i class="fas fa-bell"></i></a> 
            <p>Alerts</p>
          </div>
          <div class="card">
            <a href="#"><i class="fas fa-tint"></i></a> 
            <p>Irrigation</p>
          </div>
          <div class="card">
            <a href="#"><i class="fas fa-leaf"></i></a> 
            <p>Soil Health</p>
          </div>
          <div class="card">
            <a href="#"><i class="fas fa-rss"></i></a> 
            <p>Sensors</p>
          </div>
        </div>
      </div>
  
    </nav>
  </aside>
  
  <style>
    /* Estilos CSS para a sidebar */
    .sidebar {
      width: 250px;
      background-color: #0d1f1b;
      color: white;
      padding: 1.5rem;
      position: fixed; 
      height: 100%; 
      left: 0;
      top: 0;
      display: flex;
      flex-direction: column;
      gap: 2rem;
      font-family: Arial, sans-serif;
    }
  
    .sidebar-header h2 {
      color: #ffffff;
    }
  
    .sidebar-content h4 {
      font-size: 1.2rem;
      color: #fff;
    }
  
    .auto-scenes {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }
  
    .card {
      background-color: #162726; 
      padding: 10px;
      border-radius: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center; 
      width: 100%;
    }
  
    .toggle-option {
      display: flex;
      align-items: center;
      justify-content: space-between; 
      width: 100%; 
      color: #ffffff;
    }
  
    .settings-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr); 
      gap: 1rem;
    }
  
    /* Ícones Font Awesome */
    .fas {
      font-size: 18px; 
      color: #ffffff;
    }
  
    /* Estilos para o botão toggle */
    .switch {
      position: relative;
      display: inline-block;
      width: 40px;
      height: 20px;
    }
  
    .switch input {
      opacity: 0;
      width: 0;
      height: 0;
    }
  
    .slider {
      position: absolute;
      cursor: pointer;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #ccc;
      -webkit-transition: .4s;
      transition: .4s;
      border-radius:  34px;
    }
  
    .slider:before {
      position: absolute;
      content: "";
      height: 14px;
      width: 14px;
      border-radius: 50%;
      left: 3px;
      bottom: 3px;
      background-color: white;
      -webkit-transition: .4s;
      transition: .4s;
    }
  
    input:checked + .slider {
      background-color: #4caf50;
    }
  
    input:checked + .slider:before {
      -webkit-transform: translateX(20px);
      -ms-transform: translateX(20px);
      transform: translateX(20px);
    }
  
    .card a {
      color: #a8dadc;
    }
  
    .card p {
      color: #ffffff;
    }
  
    .card a:hover {
      color: #a8dadc;
    }
  
    .settings {
      margin-top: 2rem;
    }
  </style>