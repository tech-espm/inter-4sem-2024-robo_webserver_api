<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    let svgElement;
    let sensorData = generateSensorData();
  
    function generateSensorData() {
      return {
        temperatura: (20 + Math.random() * 10).toFixed(1),  
        soloTemp: (15 + Math.random() * 10).toFixed(1),     
        vento: (Math.random() * 10).toFixed(1),              
        precipitacao: (Math.random() * 5).toFixed(1),      
        umidade: Math.round(30 + Math.random() * 50),     
      };
    }
  
    onMount(() => {
      const cardWidth = 300;
      const cardHeight = 300;
      const chartPadding = 60;
  
      const svg = d3.select(svgElement)
        .attr('width', cardWidth)
        .attr('height', cardHeight);
  
      svg.append('rect')
        .attr('x', 0)
        .attr('y', chartPadding)
        .attr('width', cardWidth)
        .attr('height', cardHeight - chartPadding)
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
        .attr('cy', d => d.y + chartPadding)
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
        .attr('transform', d => `translate(${d.x}, ${d.y + chartPadding})`);
  
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
        .attr('x', cardWidth - 20)
        .attr('y', 40)
        .attr('text-anchor', 'end')
        .attr('fill', '#2d5a4c')
        .style('font-size', '18px')
        .attr('class', 'weather-value')
        .text(sensorData.temperatura + '°C');
    });
  
    // Atualiza os dados dos sensores sem recriar o SVG
    function updateSensorData() {
      sensorData = generateSensorData();
  
      d3.select('.weather-value').text(sensorData.temperatura + '°C');
      const circlesData = [
        { label: 'Soil temp', value: sensorData.soloTemp + ' °C' },
        { label: 'Wind', value: sensorData.vento + ' m/s' },
        { label: 'Precipitation', value: sensorData.precipitacao + ' mm' },
        { label: 'Humidity', value: sensorData.umidade + '%' }
      ];
  
      d3.selectAll('.info-circle text:nth-of-type(1)')
        .data(circlesData)
        .text(d => d.value);
  
      d3.selectAll('.info-circle text:nth-of-type(2)')
        .data(circlesData)
        .text(d => d.label);
    }
  
    setInterval(() => {
      updateSensorData();  
    }, 5000);
  </script>
  
  <div class="card">
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
      height: 300px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  
    svg {
      display: block;
      border-radius: 30px;
    }
  </style>
  