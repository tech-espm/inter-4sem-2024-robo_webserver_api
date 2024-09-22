<header class="header">
    <nav>
      <ul>
        <li><a href="#">Dashboard</a></li>
        <li><a href="#">Harvest</a></li>
        <li><a href="#">Customization</a></li>
        <li><a href="#">Settings</a></li>
      </ul>
    </nav>
    <div class="actions">
      <button class="add-member">+ Add Member</button>
      <div class="profile">
        <img src="/path-to-profile.jpg" alt="Profile">
      </div>
    </div>
  </header>
  
  <style>
    .header {
      display: flex;
      justify-content: space-between;
      padding-bottom: 1rem;
      border-bottom: 1px solid #e2e8f0;
    }
  
    nav ul {
      display: flex;
      list-style: none;
    }
  
    nav ul li {
      margin-right: 2rem;
    }
  
    nav ul li a {
      text-decoration: none;
      color: #4a4a4a;
    }
  
    .actions {
      display: flex;
      align-items: center;
    }
  
    .add-member {
      background-color: #d6394c;
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      margin-right: 1.5rem;
      border-radius: 5px;
    }
  
    .profile img {
      width: 40px;
      height: 40px;
      border-radius: 50%;
    }
  </style>
  