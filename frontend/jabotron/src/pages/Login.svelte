<script>
    let showSignUp = false;
  
    function toggleForm() {
      showSignUp = !showSignUp;
    }
  </script>
  
  <style>
  
    .container {
      position: relative;
      width: 100%;
      height: 100vh;
      display: flex;
      overflow: hidden;
    }
  
    .panel {
      width: 50%;
      height: 100%;
      position: absolute;
      display: flex;
      justify-content: center;
      align-items: center;
      transition: transform 0.5s ease-in-out;
    }
  
    .left-panel {
      background: linear-gradient(to bottom right, #6a11cb, #2575fc);
      color: white;
      z-index: 2;
      transform: translateX(0);
    }
  
    .right-panel {
      background: linear-gradient(to bottom right, #ff6a00, #ee0979);
      color: white;
      z-index: 1;
      transform: translateX(100%);
    }
  
    .form {
      background: white;
      border-radius: 10px;
      padding: 40px;
      width: 300px;
      box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
      text-align: center;
    }
  
    .form input {
      width: 100%;
      padding: 10px;
      margin-bottom: 15px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }
  
    .form button {
      background: #6a11cb;
      color: white;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.3s;
    }
  
    .form button:hover {
      background: #2575fc;
    }
  
    .toggle-btn {
      background: none;
      border: 2px solid white;
      color: white;
      padding: 10px 20px;
      border-radius: 20px;
      cursor: pointer;
      font-size: 16px;
    }
  
    .toggle-btn:hover {
      background: rgba(255, 255, 255, 0.2);
    }
  
    /* Animações */
    .shift-left {
      transform: translateX(-100%);
    }
  
    .shift-right {
      transform: translateX(0);
    }
  </style>
  
  <div class="container">
    <!-- Painel esquerdo -->
    <div class="panel left-panel" class:left-panel={showSignUp} class:shift-left={!showSignUp}>
      <div>
        <h2>New here?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Debitis!</p>
        <button class="toggle-btn" on:click={toggleForm}>Sign Up</button>
      </div>
    </div>
  
    <!-- Painel direito -->
    <div class="panel right-panel" class:right-panel={!showSignUp} class:shift-right={showSignUp}>
      <div>
        <h2>One of us?</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nostrum!</p>
        <button class="toggle-btn" on:click={toggleForm}>Sign In</button>
      </div>
    </div>
  
    <!-- Formulário -->
    <div class="form-container" class:shift-left={showSignUp}>
      {#if showSignUp}
        <div class="form">
          <h2>Sign Up</h2>
          <input type="text" placeholder="Username" />
          <input type="email" placeholder="Email" />
          <input type="password" placeholder="Password" />
          <button>Sign Up</button>
        </div>
      {:else}
        <div class="form">
          <h2>Sign In</h2>
          <input type="text" placeholder="Username" />
          <input type="password" placeholder="Password" />
          <button>Sign In</button>
        </div>
      {/if}
    </div>
  </div>
  