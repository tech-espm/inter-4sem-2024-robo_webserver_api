<script>
    let moistureLevels = [15, 30, 45, 60]; // Exemplos de dados
  </script>
  
  <section class="soil-analysis">
    <div class="header">
      <h3>Soil analysis</h3>
      <span>Details</span>
    </div>
    
    <div class="chart">
      <div class="chart-left">
        <p>pH 5.7%</p>
        <div class="soil-moisture">
          {#each moistureLevels as level}
            <div class="bar" style="height: {level}%"></div>
          {/each}
        </div>
      </div>
      <div class="chart-right">
        <div class="indicator">
          <p>Pressure</p>
          <span>101.3 kPa</span>
        </div>
        <div class="indicator">
          <p>Wind</p>
          <span>8 m/s</span>
        </div>
        <div class="indicator">
          <p>Air Quality</p>
          <span>42 AQI</span>
        </div>
      </div>
    </div>
  </section>
  
  <style>
    .soil-analysis {
      background-color: white;
      padding: 1.5rem;
      border-radius: 10px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      display: flex;
      flex-direction: column;
    }
  
    .header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 1rem;
    }
  
    .chart {
      display: flex;
      justify-content: space-between;
      gap: 2rem;
    }
  
    .chart-left {
      display: flex;
      flex-direction: column;
      align-items: center;
    }
  
    .soil-moisture {
      display: flex;
      flex-direction: row;
      height: 150px;
    }
  
    .bar {
      width: 20px;
      background-color: #4caf50;
      margin-right: 5px;
    }
  
    .chart-right {
      display: flex;
      flex-direction: column;
      justify-content: space-around;
      gap: 1rem;
    }
  
    .indicator {
      background-color: #f3f4f6;
      padding: 1rem;
      border-radius: 5px;
    }
  
    .indicator p {
      margin: 0;
    }
  
    .indicator span {
      font-weight: bold;
      font-size: 1.2rem;
    }
  </style>
  