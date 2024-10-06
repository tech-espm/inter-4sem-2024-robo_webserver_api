<script>
    const teamMembers = [
      {
        name: 'Andrezza Freire',
        role: 'Desenvolvedora Back-end',
        description: 'Desenvolvedora backend especializada em Python, com foco em APIs RESTful, automação e otimização de sistemas. Experiência em bancos de dados SQL e integração de serviços web.',
        image: './img/ANDREZZA.jpg',
        funFact: 'Rainha da coitadolândia',
        social: {
          linkedin: 'https://www.linkedin.com/in/andrezzahfreire/',
          github: 'https://github.com/andrezzahfreire'
        }
      },
      {
        name: 'Felipe Arruda',
        role: 'Engenheiro de Machine Leraning',
        description: 'Engenheiro de Machine Learning com experiência em desenvolver e implementar modelos preditivos utilizando bibliotecas como TensorFlow e Scikit-learn. Especializado em processamento de dados e otimização de algoritmos para soluções de inteligência artificial.',
        image: 'https://placehold.co/400',
        funFact: 'Soldado',
        social: {
          linkedin: 'https://www.linkedin.com/in/felipe-botelho-451418180/',
          github: 'https://github.com/FelipeBotelho94'
        }
      },
      {
        name: 'Gabriel Chaves',
        role: 'Desenvolvedor Front-End',
        description: 'Desenvolvedor frontend especializado em Svelte, com foco em criar interfaces dinâmicas e eficientes. Experiência em desenvolver aplicações web rápidas e responsivas, priorizando usabilidade e performance.',
        image: 'https://placehold.co/400',
        funFact: 'Rei do Mario Kart',
        social: {
          linkedin: '#',
          github: '#'
        }
      },
      {
        name: 'Lorena Guedes',
        role: 'Desenvolvedora Front-End',
        description: 'Desenvolvedora frontend especializada em Svelte, com foco em interfaces interativas e alto desempenho. Experiência em criar aplicações web responsivas e otimizadas para a experiência do usuário.',
        image: '/img/LORENA.jpg',
        funFact: 'Maior vascaína existente',
        social: {
          linkedin: 'https://www.linkedin.com/in/lorenaguedess/',
          github: 'https://github.com/lorenaguedes'
        }
      },
      {
        name: 'Luca Donato',
        role: 'Analista',
        description: 'Product Owner com ampla experiência em gestão de produtos digitais, focado na entrega de valor ao cliente e na otimização de processos ágeis. Especialista em definir roadmaps, priorizar backlog e alinhar equipes de desenvolvimento com as necessidades do negócio',
        image: '/img/LUCA.jpg',
        funFact: 'Engenheiro De Prompt',
        social: {
          linkedin: 'https://www.linkedin.com/in/luca-de-donato/',
          github: 'https://github.com/lucaddonato'
        }
      },
      {
        name: 'Matheus Asael',
        role: 'Engenheiro IOT',
        description: 'Engenheiro IoT com expertise em desenvolvimento de soluções utilizando Arduino, integrando sensores e automação. Experiência em conectividade de dispositivos e monitoramento remoto em tempo real.',
        image: '/img/MATHEUS.jpg',
        funFact: 'Odeia cólica e é fã da Lana Del Rey',
        social: {
          linkedin: 'https://www.linkedin.com/in/matheus-asael-silva-macedo-b57467265/',
          github: 'https://github.com/M-asael'
        }
      }
    ];
  </script>
  
  <svelte:head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css">
  </svelte:head>
  
  <div class="container py-5">
    <header class="text-center mb-5">
      <h1 class="display-4 mb-3">Sobre Nós</h1>
      <p class="lead text-muted">Conheça a nossa equipe!</p>
    </header>
  
    <div class="row g-4">
      {#each teamMembers as member, index}
        <div class="col-md-4 mb-4">
          <div class="card-container">
            <div class="card">
              <div class="card-front">
                <img src={member.image} alt={member.name} class="card-img-top">
                <div class="card-body">
                  <h5 class="card-title">{member.name}</h5>
                  <p class="card-text text-primary">{member.role}</p>
                  <div class="social-icons">
                    <a href={member.social.linkedin} class="social-icon" title="LinkedIn">
                      <i class="bi bi-linkedin"></i>
                    </a>
                    <a href={member.social.github} class="social-icon" title="GitHub">
                      <i class="bi bi-github"></i>
                    </a>
                  </div>
                </div>
              </div>
              <div class="card-back">
                <div class="card-body d-flex flex-column justify-content-center">
                  <h5 class="card-title">{member.name}</h5>
                  <p class="card-text">{member.description}</p>
                  <p class="card-text"><small class="text-primary">{member.funFact}</small></p>
                  <div class="social-icons mt-3">
                    <a href={member.social.linkedin} class="social-icon" title="LinkedIn">
                      <i class="bi bi-linkedin"></i>
                    </a>
                    <a href={member.social.github} class="social-icon" title="GitHub">
                      <i class="bi bi-github"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
  
  <style>
    .card-container {
      perspective: 1000px;
      height: 400px;
    }
  
    .card {
      position: relative;
      height: 100%;
      text-align: center;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      cursor: pointer;
      border: none;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
  
    .card-container:hover .card {
      transform: rotateY(180deg);
    }
  
    .card-front, .card-back {
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      border-radius: 10px;
      overflow: hidden;
    }
  
    .card-front {
      background-color: white;
    }
  
    .card-back {
      background-color: white;
      transform: rotateY(180deg);
      display: flex;
      align-items: center;
    }
  
    .card-img-top {
      height: 250px;
      object-fit: cover;
    }
  
    .social-icons {
      display: flex;
      justify-content: center;
      gap: 15px;
      margin-top: 10px;
    }
  
    .social-icon {
      font-size: 1.5rem;
      color: #0077b5; 
      transition: color 0.3s ease;
    }
  
    .social-icon:hover {
      color: #005885;
    }
  
    .social-icon .bi-github {
      color: #333; 
    }
  
    .social-icon:hover .bi-github {
      color: #000;
    }
  
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(20px); }
      to { opacity: 1; transform: translateY(0); }
    }
  
    .col-md-4 {
      animation: fadeIn 0.5s ease forwards;
    }
  
    .col-md-4:nth-child(1) { animation-delay: 0.1s; }
    .col-md-4:nth-child(2) { animation-delay: 0.2s; }
    .col-md-4:nth-child(3) { animation-delay: 0.3s; }
    .col-md-4:nth-child(4) { animation-delay: 0.4s; }
    .col-md-4:nth-child(5) { animation-delay: 0.5s; }
    .col-md-4:nth-child(6) { animation-delay: 0.6s; }
  </style>