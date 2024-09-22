<script>
    
    let autoIrrigation = true;
    let frostProtection = false;
  </script>
  
  <aside class="sidebar">
    <div class="logo">
      <img src="/path-to-logo.png" alt="Logo" />
      <h2>Jabotron</h2>
    </div>
  
    <nav>
      <div class="auto-scenes">
        <h4>Auto scenes</h4>
        <div class="toggle-option">
          <span>Auto irrigation</span>
          <label class="switch">
            <input type="checkbox" bind:checked={autoIrrigation} />
            <span class="slider round"></span>
          </label>
        </div>
        <div class="toggle-option">
          <span>Frost Protection</span>
          <label class="switch">
            <input type="checkbox" bind:checked={frostProtection} />
            <span class="slider round"></span>
          </label>
        </div>
      </div>
  
      <div class="settings">
        <h4>Settings</h4>
        <ul>
          <li><a href="#">Alerts</a></li>
          <li><a href="#">Irrigation</a></li>
          <li><a href="#">Soil Health</a></li>
          <li><a href="#">Sensors</a></li>
          <li><a href="#">Scenes</a></li>
        </ul>
      </div>
    </nav>
  </aside>
  
  <style>
    .sidebar {
      width: 250px;
      background-color: #22333b;
      color: white;
      padding: 1.5rem;
      position: fixed;
      height: 100%;
      left: 0;
      top: 0;
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }
  
    .logo {
      display: flex;
      align-items: center;
      gap: 1rem;
    }
  
    .logo img {
      width: 40px;
      height: 40px;
    }
  
    .logo h2 {
      font-size: 1.5rem;
      font-weight: bold;
    }
  
    nav h4 {
      margin-bottom: 1rem;
      font-size: 1.2rem;
    }
  
    .auto-scenes,
    .settings {
      margin-bottom: 2rem;
    }
  
    .toggle-option {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.2rem;
    }
  
    .toggle-option span {
      font-size: 1rem;
    }
  
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
      transition: 0.4s;
      border-radius: 34px;
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
      transition: 0.4s;
    }
  
    input:checked + .slider {
      background-color: #4caf50;
    }
  
    input:checked + .slider:before {
      transform: translateX(20px);
    }
  
    nav ul {
      list-style: none;
      padding: 0;
    }
  
    nav ul li {
      margin-bottom: 1rem;
    }
  
    nav ul li a {
      color: #fff;
      text-decoration: none;
      font-size: 1rem;
      display: flex;
      align-items: center;
    }
  
    nav ul li a:hover {
      color: #a8dadc;
    }
  </style>