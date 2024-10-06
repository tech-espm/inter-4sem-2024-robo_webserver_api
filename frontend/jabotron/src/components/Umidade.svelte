<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
  
    const data = [
      { category: 'Low', fields: 15, color: '#ffb3b3', fillColor: '#ff8080' },
      { category: 'Optimal', fields: 32, color: '#b3ffb3', fillColor: '#4dff4d' },
      { category: 'High', fields: 28, color: '#b3d9ff', fillColor: '#4da6ff' }
    ];
  
    let svgElement;
  
    onMount(() => {
      const width = 300;
      const height = 300;
      const margin = { top: 20, right: 20, bottom: 40, left: 40 };
  
      const innerWidth = width - margin.left - margin.right;
      const innerHeight = height - margin.top - margin.bottom;
  
      const svg = d3.select(svgElement)
        .attr('width', width)
        .attr('height', height);
  
      const g = svg.append('g')
        .attr('transform', `translate(${margin.left},${margin.top})`);
  
      const xScale = d3.scaleBand()
        .domain(data.map(d => d.category))
        .range([0, innerWidth])
        .padding(0.3);
  
      const yScale = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.fields)])
        .range([innerHeight, 0]);
  
      data.forEach(d => {
        const barGroup = g.append('g');
        
        // Background bar
        barGroup.append('rect')
          .attr('x', xScale(d.category))
          .attr('y', 0)
          .attr('width', xScale.bandwidth())
          .attr('height', innerHeight)
          .attr('fill', d.color)
          .attr('rx', 4);
  
        // Foreground bar
        const barHeight = innerHeight - yScale(d.fields);
        barGroup.append('rect')
          .attr('x', xScale(d.category))
          .attr('y', innerHeight - barHeight)
          .attr('width', xScale.bandwidth())
          .attr('height', barHeight)
          .attr('fill', d.fillColor)
          .attr('rx', 4);
  
        // Category label
        barGroup.append('text')
          .attr('x', xScale(d.category) + xScale.bandwidth() / 2)
          .attr('y', innerHeight + 25)
          .attr('text-anchor', 'middle')
          .attr('class', 'category-label')
          .text(d.category);
  
        // Fields count
        barGroup.append('text')
          .attr('x', xScale(d.category) + xScale.bandwidth() / 2)
          .attr('y', -10)
          .attr('text-anchor', 'middle')
          .attr('class', 'fields-count')
          .text(`${d.fields} Fields`);
      });
    });
  </script>
  
  <div class="card">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-center mb-3">
        <h5 class="card-title">Soil moisture</h5>
        <span class="badge bg-light text-dark rounded-pill">Today</span>
      </div>
      <svg bind:this={svgElement}></svg>
    </div>
  </div>
  
  <style>
    .card {
    width: 300px;
      margin: 1rem;
      border-radius: 30px;
    }
    :global(.category-label) {
      font-size: 14px;
      fill: #6c757d;
    }
    :global(.fields-count) {
      font-size: 14px;
      font-weight: 600;
    }
  </style>