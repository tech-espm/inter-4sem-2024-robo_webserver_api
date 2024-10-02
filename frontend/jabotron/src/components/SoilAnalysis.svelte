<script>
  import { onMount } from "svelte";
  import * as d3 from "d3";

  let moistureLevels = [15, 30, 45, 60]; // Exemplos de dados
  let pressure = 101.3; // kPa
  let wind = 8; // m/s
  let airQuality = 42; // AQI

  onMount(() => {
    function createArcIndicator(selector, value, maxValue, color, unit = "") {
      const width = 100;
      const height = 100;
      const radius = Math.min(width, height) / 2;

      const svg = d3
        .select(selector)
        .append("svg")
        .attr("width", 150)
        .attr("height", 150)
        .append("g")
        .attr("transform", `translate(${width / 2}, ${height / 2})`);

      const arc = d3
        .arc()
        .innerRadius(radius - 20)
        .outerRadius(radius)
        .startAngle(0)
        .endAngle((value / maxValue) * 2 * Math.PI);

      svg.append("path").attr("d", arc).attr("fill", color);

      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "central")
        .text(value.toFixed(1) + unit) // Formata o valor
        .style("font-size", "14px");
    }

    createArcIndicator(".indicator-pressure", pressure, 150, "#2196f3", " kPa");
    createArcIndicator(".indicator-wind", wind, 20, "#ff9800", " m/s");
    createArcIndicator(
      ".indicator-air-quality",
      airQuality,
      100,
      "#f44336",
      " AQI",
    );
  });
</script>

<section class="soil-analysis">
  <div class="header">
    <h3>Soil analysis</h3>
    <span>Details</span>
  </div>

  <div class="chart">
    <div class="chart-left">
      <div class="soil-moisture">
        <div class="moisture-levels">
          <span>15%</span>
          <span>30%</span>
          <span>45%</span>
          <span>60%</span>
        </div>
      </div>
    </div>
    <div class="chart-right">
      <div class="indicators-container">
        <div class="indicator indicator-pressure"></div>
        <div class="indicator indicator-wind"></div>
        <div class="indicator indicator-air-quality"></div>
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

  .chart-right {
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .indicators-container {
    display: flex;
    gap: 1rem;
  }

  .indicator {
    padding: 1rem;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 150px;
    height: 150px;
  }
  .moisture-levels {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 1rem;
}

.moisture-levels span {
  font-size: 14px;
  margin-bottom: 0.5rem;
}
</style>
