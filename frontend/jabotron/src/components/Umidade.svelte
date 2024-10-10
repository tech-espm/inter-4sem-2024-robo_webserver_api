<script>
    import { onMount } from "svelte";
    import flatpickr from "flatpickr";
    import "flatpickr/dist/flatpickr.min.css";
    import * as d3 from "d3";

    let svgElement;
    let selectedDate = "Today";

    let data = [
        {
            category: "Baixa",
            color: "#FEE7E7",
            fillColor: "#F99D9E",
            topFaceColor: "#F66769",
            filledRatio: 0.4,
        },
        {
            category: "Ótima",
            color: "#E7FDF3",
            fillColor: "#7DF5BC",
            topFaceColor: "#39F098",
            filledRatio: 0.8,
        },
        {
            category: "Alta",
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
            onChange: (selectedDates, dateStr) => {
                selectedDate = dateStr || "Today";
                updateData();
            },
        });
        drawChart();
    });

    function drawChart() {
        d3.select(svgElement).selectAll("*").remove();

        const width = 300;
        const height = 250;
        const margin = { top: 40, right: 40, bottom: 30, left: 0 };

        const innerWidth = width - margin.left - margin.right;
        const innerHeight = height - margin.top - margin.bottom;

        const svg = d3
            .select(svgElement)
            .attr("width", "100%")
            .attr("height", height)
            .style("display", "block")
            .style("margin", "0 auto");

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
    }
</script>

<div class="card">
    <div class="card-body">
        <div class="header">
            <h5 class="chart-title">Umidade do Solo</h5>
            <button class="date-picker">
                {selectedDate}
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-calendar" viewBox="0 0 16 16">
                    <path d="M3.5 0a.5.5 0 0 1 .5.5V1h9V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H1a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5zM1 4v10a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V4H1z"/>
                </svg>
            </button>
        </div>
        <svg bind:this={svgElement}></svg>
    </div>
</div>

<style>
    .card {
        width: 90%;
        max-width: 500px;
        border: 1px solid #ddd;
        border-radius: 30px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        margin: 1rem auto;
        transition: box-shadow 0.3s ease;
    }

    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .chart-title {
        font-size: 18px;
        font-weight: bold;
        color: #2d5a4c;
        margin: 15px 0;
    }

    .card:hover {
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }

    .date-picker {
        appearance: none;
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 30px;
        padding: 8px 35px 8px 15px;
        font-size: 14px;
        color: #333;
        cursor: pointer;
        transition: all 0.2s;
        display: flex;
        align-items: center;
    }

    svg {
        width: 100%;
        height: auto;
    }
</style>
