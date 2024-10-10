<script>
  import { onMount } from 'svelte';
  import * as d3 from 'd3';

  let svgElement;
  let containerDiv;
  let sensorData = generateSensorData();
  const baseWidth = 300; 
  const baseHeight = 300;
  let currentWidth = baseWidth;
  let currentHeight = baseHeight;

  function generateSensorData() {
    return {
      temperatura: (20 + Math.random() * 10).toFixed(1),
      soloTemp: (15 + Math.random() * 10).toFixed(1),
      vento: (Math.random() * 10).toFixed(1),
      precipitacao: (Math.random() * 5).toFixed(1),
      umidade: Math.round(30 + Math.random() * 50),
    };
  }

  function updateVisualization() {
    if (!containerDiv) return;

    const containerRect = containerDiv.getBoundingClientRect();
    const scale = Math.min(containerRect.width / baseWidth, 1);
    currentWidth = baseWidth * scale;
    currentHeight = baseHeight * scale;
    
    const chartPadding = 60 * scale;

    d3.select(svgElement).selectAll("*").remove();

    const svg = d3.select(svgElement)
      .attr('width', currentWidth)
      .attr('height', currentHeight)
      .attr('viewBox', `0 0 ${baseWidth} ${baseHeight}`);

    svg.append('rect')
      .attr('x', 0)
      .attr('y', 60)
      .attr('width', baseWidth)
      .attr('height', baseHeight - 60)
      .attr('fill', '#2d5a4c')
      .attr('rx', 30)
      .attr('ry', 30);

    const backgroundCircles = [
      { x: 5, y: 90, r: 30 },
      { x: 50, y: 110, r: 15 },
      { x: 70, y: 10, r: 60 },
      { x: 210, y: 10, r: 70 },
      { x: 190, y: 170, r: 20 },
      { x: 205, y: 110, r: 15 },
      { x: 225, y: 175, r: 10 },
      { x: 250, y: 240, r: 55 },
    ];

    svg.selectAll('.background-circle')
      .data(backgroundCircles)
      .enter()
      .append('circle')
      .attr('cx', d => d.x)
      .attr('cy', d => d.y + 60)
      .attr('r', d => d.r)
      .attr('fill', 'rgba(255, 255, 255, 0.15)');

    const circles = svg.selectAll('.info-circle')
      .data([
        { label: 'Solo Temp', value: sensorData.soloTemp + ' °C', x: 130, y: 120, r: 55 },
        { label: 'Vento', value: sensorData.vento + ' m/s', x: 270, y: 130, r: 50 },
        { label: 'Precipitação', value: sensorData.precipitacao + ' mm', x: 30, y: 200, r: 70 },
        { label: 'Umidade', value: sensorData.umidade + '%', x: 145, y: 220, r: 40},
      ])
      .enter()
      .append('g')
      .attr('transform', d => `translate(${d.x}, ${d.y + 60})`);

    circles.append('circle')
      .attr('r', d => d.r)
      .attr('fill', 'rgba(255, 255, 255, 0.8)');

    circles.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '-0.5em')
      .attr('fill', 'black')
      .style('font-size', '12px')
      .text(d => d.value);

    circles.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '1.5em')
      .attr('fill', '#555')
      .style('font-size', '10px')
      .text(d => d.label);

    svg.append('text')
      .attr('x', 20)
      .attr('y', 40)
      .attr('fill', '#2d5a4c')
      .style('font-size', '18px')
      .style('font-weight', 'bold')
      .attr('class', 'temperature-label')
      .text('Temperatura');

    svg.append('text')
      .attr('x', baseWidth - 20)
      .attr('y', 40)
      .attr('text-anchor', 'end')
      .attr('fill', '#415B4E')
      .style('font-size', '18px')
      .attr('class', 'weather-value')
      .text(sensorData.temperatura + '°C');
  }

  function updateSensorData() {
    sensorData = generateSensorData();
    updateVisualization();
  }

  onMount(() => {
    const resizeObserver = new ResizeObserver(() => {
      updateVisualization();
    });
    resizeObserver.observe(containerDiv);

    setInterval(updateSensorData, 5000);

    return () => {
      resizeObserver.disconnect();
    };
  });
</script>

<div class="card" bind:this={containerDiv}>
  <svg bind:this={svgElement}></svg>
</div>

<style>
  .card {
    background-color: white;
    border-radius: 30px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    padding: 0;
    margin: 1rem;
    width: 300px;
    max-width: 100%;
    aspect-ratio: 1;
    display: flex;
    justify-content: center;
    align-items: center;
    transition: box-shadow 0.3s ease;
  }

  svg {
    display: block;
    max-width: 100%;
    height: auto;
    border-radius: 30px;
  }
  
  .card:hover {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
  }

  @media (max-width: 340px) {
    .card {
      margin: 0.5rem;
      border-radius: 30px;
    }
  }
</style>