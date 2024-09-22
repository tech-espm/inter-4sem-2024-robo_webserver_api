<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    let soilAnalysisChart;
    let moistureLevelsChart;
  
    onMount(() => {
      createBasicLineChart(soilAnalysisChart);
      createBasicLineChart(moistureLevelsChart);
    });
  
    function createBasicLineChart(chart) {
      const svg = d3.select(chart)
        .append("svg")
        .attr("width", "100%")
        .attr("height", 200);
  
      const data = [10, 15, 20, 25, 30, 35, 40];
  
      svg.selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", (d, i) => i * 40 + 20)
        .attr("cy", d => 200 - d * 4)
        .attr("r", 5)
        .style("fill", "#28a745");
    }
  </script>
  
  <div class="container-fluid">
    <!-- Sidebar -->
    <div class="sidebar p-3">
      <h2 class="text-center mb-4">AgriNex</h2>
      <nav>
        <a href="#" class="nav-link">Dashboard</a>
        <a href="#" class="nav-link">Harvest</a>
        <a href="#" class="nav-link">Customization</a>
        <a href="#" class="nav-link">Settings</a>
      </nav>
    </div>
  
    <!-- Main Content -->
    <div class="main-content">
      <div class="header mb-4">
        <h3>Soil Analysis Dashboard</h3>
        <button class="btn btn-primary">+ Add Member</button>
      </div>
  
      <div class="row">
        <!-- Cards Section -->
        <div class="col-md-6 mb-4">
          <div class="card card-custom p-3">
            <h5>Soil Analysis</h5>
            <div bind:this={soilAnalysisChart} class="chart-container"></div>
          </div>
        </div>
  
        <div class="col-md-6 mb-4">
          <div class="card card-custom p-3">
            <h5>Soil Moisture Levels</h5>
            <div bind:this={moistureLevelsChart} class="chart-container"></div>
          </div>
        </div>
      </div>
  
      <div class="row">
        <!-- More Cards Section -->
        <div class="col-md-6 mb-4">
          <div class="card card-custom p-3">
            <h5>Nutrients Levels</h5>
            <ul class="list-group list-group-flush">
              <li class="list-group-item">Magnesium: 0.20 - 0.30</li>
              <li class="list-group-item">Acidity (pH): 5.5 - 7.5</li>
              <li class="list-group-item">Phosphorus: 0.10 - 0.30</li>
              <li class="list-group-item">Potassium: 110 - 280 kg</li>
              <li class="list-group-item">Organic Carbon: 0.5 - 7.5</li>
            </ul>
          </div>
        </div>
  
        <div class="col-md-6 mb-4">
          <div class="card card-custom p-3">
            <h5>Growing Flow</h5>
            <img src="https://via.placeholder.com/300x150" alt="Growing Flow" class="img-fluid rounded">
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <style>
    .sidebar {
      height: 100vh;
      width: 220px;
      position: fixed;
      background-color: #0b3d3e;
      color: white;
      padding-top: 10px;
    }
    .sidebar a {
      color: white;
      text-decoration: none;
      margin: 10px 0;
      display: block;
    }
    .main-content {
      margin-left: 240px;
      padding: 20px;
    }
    .card-custom {
      border-radius: 15px;
      background-color: #f5f5f5;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .chart-container {
      width: 100%;
      height: 200px;
    }
    .header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: #f8f9fa;
      padding: 10px 20px;
      border-radius: 10px;
    }
  </style>
  