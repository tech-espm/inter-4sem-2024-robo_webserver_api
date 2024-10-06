<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    import { writable } from 'svelte/store';

    // Dados semanais
    const weeklyData = [
        { year: 2024.0, weekday: 'Segunda', Nitrogênio: 38, Fósforo: 48, Potássio: 43 },
        { year: 2024.2, weekday: 'Terça', Nitrogênio: 39, Fósforo: 49, Potássio: 44 },
        { year: 2024.4, weekday: 'Quarta', Nitrogênio: 40, Fósforo: 50, Potássio: 45 },
        { year: 2024.6, weekday: 'Quinta', Nitrogênio: 41, Fósforo: 51, Potássio: 46 },
        { year: 2024.8, weekday: 'Sexta', Nitrogênio: 42, Fósforo: 52, Potássio: 47 }
    ];

    // Dados mensais
    const monthlyData = [
        { year: 2020, month: 'Jan', Nitrogênio: 20, Fósforo: 30, Potássio: 25 },
        { year: 2021, month: 'Mar', Nitrogênio: 25, Fósforo: 35, Potássio: 30 },
        { year: 2022, month: 'Jun', Nitrogênio: 30, Fósforo: 40, Potássio: 35 },
        { year: 2023, month: 'Set', Nitrogênio: 35, Fósforo: 45, Potássio: 40 },
        { year: 2024, month: 'Dez', Nitrogênio: 40, Fósforo: 50, Potássio: 45 }
    ];

    // Dados trimestrais
    const quarterlyData = [
        { year: 2023.0, quarter: '1º Tri', Nitrogênio: 32, Fósforo: 42, Potássio: 37 },
        { year: 2023.25, quarter: '2º Tri', Nitrogênio: 34, Fósforo: 44, Potássio: 39 },
        { year: 2023.5, quarter: '3º Tri', Nitrogênio: 36, Fósforo: 46, Potássio: 41 },
    ];

    const lineData = [
        { name: "Nitrogênio", color: "#b3e5fc" },
        { name: "Fósforo", color: "#ffe0b2" },
        { name: "Potássio", color: "#ffccbc" }
    ];

    let svgElement;
    const interval = writable('mensalmente');
    let currentData = monthlyData;

    function getLabelForAxis(interval) {
        switch(interval) {
            case 'semanalmente':
                return d => d.weekday;
            case 'mensalmente':
                return d => d.month;
            case 'trimestralmente':
                return d => d.quarter;
        }
    }

    function updateChart() {
        const selectedInterval = $interval;
        
        // Atualiza os dados baseado no intervalo selecionado
        switch(selectedInterval) {
            case 'semanalmente':
                currentData = weeklyData;
                break;
            case 'mensalmente':
                currentData = monthlyData;
                break;
            case 'trimestralmente':
                currentData = quarterlyData;
                break;
        }

        const margin = { top: 20, right: 170, bottom: 30, left: 40 }; // Aumentei a margem direita
        const width = 600;
        const height = 220;
        const chartWidth = width - margin.left - margin.right;
        const chartHeight = height - margin.top - margin.bottom;

        d3.select(svgElement).selectAll("*").remove();

        const svg = d3.select(svgElement)
            .attr("width", width)
            .attr("height", height)
            .append("g")
            .attr("transform", `translate(${margin.left}, ${margin.top})`);

        // Escalas
        const xScale = d3.scalePoint()
            .domain(currentData.map(getLabelForAxis(selectedInterval)))
            .range([0, chartWidth]);

        const yScale = d3.scaleLinear()
            .domain([0, d3.max(currentData, d => 
                Math.max(d.Nitrogênio, d.Fósforo, d.Potássio)
            ) + 5])
            .range([chartHeight, 0]);

        // Eixos
        svg.append("g")
            .attr("transform", `translate(0, ${chartHeight})`)
            .call(d3.axisBottom(xScale))
            .style("font-size", "10px")
            .selectAll("text")  
            .style("text-anchor", "end")
            .attr("dx", "-.8em")
            .attr("dy", ".15em")
            .attr("transform", "rotate(-45)"); // Rotaciona os rótulos para melhor legibilidade

        svg.append("g")
            .call(d3.axisLeft(yScale))
            .style("font-size", "12px");

        // Gerador de linhas
        const lineGenerator = d3.line()
            .curve(d3.curveCatmullRom)
            .x(d => xScale(getLabelForAxis(selectedInterval)(d)))
            .y(d => yScale(d.value));

        // Adiciona as linhas com animação
        lineData.forEach(line => {
            const lineDataPoints = currentData.map(d => ({
                ...d,
                value: d[line.name]
            }));

            const path = svg.append("path")
                .datum(lineDataPoints)
                .attr("class", "line")
                .attr("d", lineGenerator)
                .style("fill", "none")
                .style("stroke", line.color)
                .style("stroke-width", 2.5)
                .style("opacity", 0.8);

            // Animação da linha
            const pathLength = path.node().getTotalLength();
            path
                .attr("stroke-dasharray", pathLength + " " + pathLength)
                .attr("stroke-dashoffset", pathLength)
                .transition()
                .duration(1000)
                .ease(d3.easeLinear)
                .attr("stroke-dashoffset", 0);

            // Adiciona pontos
            svg.selectAll(`.point-${line.name}`)
                .data(lineDataPoints)
                .enter().append("circle")
                .attr("class", `point-${line.name}`)
                .attr("cx", d => xScale(getLabelForAxis(selectedInterval)(d)))
                .attr("cy", d => yScale(d[line.name]))
                .attr("r", 4)
                .style("fill", line.color)
                .style("stroke", "white")
                .style("stroke-width", 2);

            // Adiciona rótulo ao último ponto
            const lastPoint = lineDataPoints[lineDataPoints.length - 1];
            svg.append("text")
                .attr("x", xScale(getLabelForAxis(selectedInterval)(lastPoint)) + 5)
                .attr("y", yScale(lastPoint[line.name]))
                .text(lastPoint[line.name])
                .style("fill", line.color)
                .style("font-size", "12px")
                .style("font-weight", "bold")
                .attr("alignment-baseline", "middle");
        });

        // Adiciona legenda mais para o lado
        const legend = svg.append("g")
            .attr("class", "legend")
            .attr("transform", `translate(${chartWidth + 40}, 0)`); // Aumentei o deslocamento horizontal

        lineData.forEach((line, i) => {
            const legendItem = legend.append("g")
                .attr("transform", `translate(0, ${i * 25})`);

            legendItem.append("circle")
                .attr("r", 6)
                .style("fill", line.color);

            legendItem.append("text")
                .attr("x", 15)
                .attr("y", 0)
                .attr("dy", ".35em")
                .style("fill", "#666")
                .style("font-size", "12px")
                .text(line.name);
        });
    }

    onMount(() => {
        updateChart();
    });

    function changeInterval(event) {
        interval.set(event.target.value);
        updateChart();
    }
</script>

<div class="card">
    <div class="header">
        <h2 class="chart-title">Nível de Nutrientes</h2>
        <div class="dropdown">
            <select on:change={changeInterval} class="select-styled">
                <option value="semanalmente">Semanalmente</option>
                <option value="mensalmente" selected>Mensalmente</option>
                <option value="trimestralmente">Trimestralmente</option>
            </select>
        </div>
    </div>
    <div class="chart-container">
        <svg bind:this={svgElement}></svg>
    </div>
</div>

<style>
    .card {
        background-color: white;
        border-radius: 30px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        padding: 0;
        margin: 1rem;
        margin-left: -150px;
        width: 600px;
        height: 300px;
        display: flex;
        flex-direction: column;
        transition: box-shadow 0.3s ease;
    }

    .card:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px 20px;
    }

    .chart-title {
        font-size: 18px;
        font-weight: bold;
        color: #2d5a4c;
        margin: 15px 0;
    }

    .chart-container {
        flex-grow: 1;
        position: relative;
    }

    .select-styled {
        appearance: none;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 20px;
        padding: 8px 35px 8px 15px;
        font-size: 14px;
        color: #333;
        cursor: pointer;
        transition: all 0.2s;
        background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='%23333' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
        background-repeat: no-repeat;
        background-position: right 8px center;
        background-size: 16px;
    }

    .select-styled:hover, .select-styled:focus {
        border-color: #4caf50;
        box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.1);
        outline: none;
    }

    @media (max-width: 768px) {
        .card {
            margin-left: 0;
            width: 100%;
        }

        .header {
            flex-direction: column;
            align-items: flex-start;
        }

        .dropdown {
            width: 100%;
            margin-top: 10px;
        }

        .select-styled {
            width: 100%;
        }
    }
</style>