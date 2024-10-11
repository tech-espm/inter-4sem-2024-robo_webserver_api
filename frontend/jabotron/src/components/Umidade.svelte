<script>
    import { onMount } from "svelte";
    import flatpickr from "flatpickr";
    import "flatpickr/dist/flatpickr.min.css";
    import * as d3 from "d3";

    let svgElement;
    let selectedDate = new Date().toISOString().split('T')[0];

    let data = [
        {
            category: "Baixa",
            label: "Baixo",
            color: "#FEE7E7",
            fillColor: "#F99D9E",
            topFaceColor: "#F66769",
            filledRatio: 0.4,
        },
        {
            category: "Ótima",
            label: "Ótimo",
            color: "#E7FDF3",
            fillColor: "#7DF5BC",
            topFaceColor: "#39F098",
            filledRatio: 0.8,
        },
        {
            category: "Alta",
            label: "Alto",
            color: "#E8F3F6",
            fillColor: "#81BED0",
            topFaceColor: "#3C9AB6",
            filledRatio: 0.7,
        },
    ];

    function updateData() {
        data = data.map((d) => ({
            ...d,
            filledRatio: Math.random().toFixed(2),
        }));
        drawChart();
    }

    onMount(() => {
        flatpickr(".date-picker", {
            defaultDate: "today",
            maxDate: "today",
            dateFormat: "Y-m-d",
            onChange: (selectedDates, dateStr) => {
                selectedDate = dateStr;
                updateData();
            },
        });
        drawChart();
    });

    function drawChart() {
        if (!svgElement) return;

        d3.select(svgElement).selectAll("*").remove();

        const width = 300;
        const height = 300;
        const margin = { 
            top: 10, 
            right: 30, 
            bottom: 100, 
            left: 20 
        };

        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        const svg = d3
            .select(svgElement)
            .attr("width", width)
            .attr("height", height);

        const g = svg
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const xScale = d3
            .scaleBand()
            .domain(data.map((d) => d.category))
            .range([0, innerWidth])
            .padding(0.4);

        const barWidth = xScale.bandwidth();
        const barHeight = innerHeight;
        const barDepth = 15;

        data.forEach((d) => {
            const barGroup = g.append("g");

            const filledBarHeight = barHeight * d.filledRatio;

            // Back face (empty part)
            barGroup
                .append("rect")
                .attr("x", xScale(d.category) + barDepth)
                .attr("y", barDepth)
                .attr("width", barWidth)
                .attr("height", barHeight)
                .attr("fill", d3.rgb(d.color).darker(0.3));

            // Left face (empty)
            barGroup
                .append("polygon")
                .attr(
                    "points",
                    `${xScale(d.category)},0
                     ${xScale(d.category) + barDepth},${barDepth}
                     ${xScale(d.category) + barDepth},${barHeight + barDepth}
                     ${xScale(d.category)},${barHeight}`
                )
                .attr("fill", d3.rgb(d.color).darker(0.1));

            // Right face (empty)
            barGroup
                .append("polygon")
                .attr(
                    "points",
                    `${xScale(d.category) + barWidth},0 
                     ${xScale(d.category) + barWidth + barDepth},${barDepth} 
                     ${xScale(d.category) + barWidth + barDepth},${barHeight + barDepth}
                     ${xScale(d.category) + barWidth},${barHeight}`
                )
                .attr("fill", d3.rgb(d.color).darker(0.2));

            // Top face (empty)
            barGroup
                .append("polygon")
                .attr(
                    "points",
                    `${xScale(d.category)},0
                     ${xScale(d.category) + barWidth},0
                     ${xScale(d.category) + barWidth + barDepth},${barDepth}
                     ${xScale(d.category) + barDepth},${barDepth}`
                )
                .attr("fill", d3.rgb(d.color).brighter(0.2));

            // Filled part - 3D faces
            barGroup
                .append("rect")
                .attr("x", xScale(d.category) + barDepth)
                .attr("y", barHeight - filledBarHeight + barDepth)
                .attr("width", barWidth)
                .attr("height", filledBarHeight)
                .attr("fill", d.fillColor);

            barGroup
                .append("rect")
                .attr("x", xScale(d.category))
                .attr("y", barHeight - filledBarHeight)
                .attr("width", barWidth)
                .attr("height", filledBarHeight)
                .attr("fill", d.fillColor);

            barGroup
                .append("polygon")
                .attr(
                    "points",
                    `${xScale(d.category)},${barHeight - filledBarHeight}
                     ${xScale(d.category) + barDepth},${barHeight - filledBarHeight + barDepth}
                     ${xScale(d.category) + barDepth},${barHeight + barDepth}
                     ${xScale(d.category)},${barHeight}`
                )
                .attr("fill", d3.rgb(d.fillColor));

            barGroup
                .append("polygon")
                .attr(
                    "points",
                    `${xScale(d.category) + barWidth},${barHeight - filledBarHeight}
                     ${xScale(d.category) + barWidth + barDepth},${barHeight - filledBarHeight + barDepth}
                     ${xScale(d.category) + barWidth + barDepth},${barHeight + barDepth}
                     ${xScale(d.category) + barWidth},${barHeight}`
                )
                .attr("fill", d3.rgb(d.fillColor));

            barGroup
                .append("polygon")
                .attr(
                    "points",
                    `${xScale(d.category)},${barHeight - filledBarHeight}
                     ${xScale(d.category) + barWidth},${barHeight - filledBarHeight}
                     ${xScale(d.category) + barWidth + barDepth},${barHeight - filledBarHeight + barDepth}
                     ${xScale(d.category) + barDepth},${barHeight - filledBarHeight + barDepth}`
                )
                .attr("fill", d.topFaceColor);
        });

        // Add labels below bars
        data.forEach((d) => {
            g.append("text")
                .attr("x", xScale(d.category) + barWidth / 2 + barDepth / 2)
                .attr("y", height - margin.top - margin.bottom + 40)
                .attr("text-anchor", "middle")
                .attr("fill", "#2d5a4c")
                .style("font-size", "12px")
                .text(d.label);
        });
    }
</script>

<div class="card">
    <div class="card-body">
        <div class="header">
            <h5 class="chart-title">Umidade do Solo</h5>
            <div class="date-picker-container">
                <input type="text" class="date-picker" value={selectedDate}>
            </div>
        </div>
        <div class="chart-container">
            <svg bind:this={svgElement}></svg>
        </div>
    </div>
</div>

<style>
    .card {
        width: 300px;
        height: 300px;
        border: 1px solid #ddd;
        border-radius: 30px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin: 1rem auto;
        transition: box-shadow 0.3s ease;
        margin-left: 1rem;
    }

    .card-body {
        padding: 0;
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 10px 15px;
        flex-wrap: nowrap;
    }

    .chart-title {
        font-size: 16px;
        font-weight: bold;
        color: #2d5a4c;
        margin: 0;
        white-space: nowrap;
    }

    .date-picker-container {
        flex-shrink: 0;
    }

    .card:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .date-picker {
        appearance: none;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 15px;
        padding: 4px 8px;
        font-size: 10px;
        color: #333;
        cursor: pointer;
        transition: all 0.2s;
    }

    .chart-container {
        flex-grow: 1;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    :global(.flatpickr-calendar) {
        font-size: 12px !important;
        width: 200px !important;
    }

    :global(.flatpickr-current-month) {
        font-size: 12px !important;
        padding: 0 !important;
    }

    :global(.flatpickr-monthDropdown-months) {
        font-size: 12px !important;
    }

    :global(.flatpickr-day) {
        font-size: 11px !important;
        line-height: 24px !important;
        height: 24px !important;
        width: 24px !important;
        max-width: 24px !important;
    }
</style>