<template>
  <div class="info-container animate-fade-in">
    <div class="static-background">
      <div class="moving-gradient"></div>
    </div>
    
    <div class="info-content">
      <h1 class="main-title">О проекте</h1>
      
      <div class="info-card">
        <div class="creators-section">
          <h2 class="section-title">Создатели</h2>
          <div class="creators-list">
            <p>Кузора Артем 241-321</p>
            <p>Целобанов Николай 241-321</p>
          </div>
        </div>

        <div class="stack-section">
          <h2 class="section-title">Стек</h2>
          <div class="stack-list">
            <div class="stack-item">Vue.js</div>
            <div class="stack-item">Python Flask</div>
            <div class="stack-item">PostgreSQL</div>
            <div class="stack-item">Pinia</div>
            <div class="stack-item">Axios</div>
          </div>
        </div>

        <div class="github-section">
          <h2 class="section-title">GitHub</h2>
          <a class="github-button" href="https://github.com/isuaji/crownbaby">
            Перейти в репозиторий
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.info-container {
  min-height: 100vh;
  padding: 2rem;
  background-color: #000000;
  display: flex;
  justify-content: center;
  align-items: center;
}

.static-background {
  position: fixed;
  inset: 0;
  background: linear-gradient(45deg, #000000, #0f172a);
  z-index: 0;
}

.moving-gradient {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(96, 165, 250, 0.15), transparent 70%);
  animation: pulse 10s ease-in-out infinite;
}

.info-content {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 600px;
  text-align: center;
}

.main-title {
  font-size: 2.5rem;
  font-weight: 800;
  background: linear-gradient(135deg, #60a5fa 0%, #93c5fd 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 2rem;
}

.info-card {
  background: rgba(15, 23, 42, 0.6);
  border-radius: 16px;
  border: 1px solid rgba(96, 165, 250, 0.1);
  padding: 2rem;
  backdrop-filter: blur(10px);
}

.section-title {
  color: #fff;
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.creators-section {
  margin-bottom: 2rem;
}

.creators-list {
  color: #94a3b8;
  font-size: 1.1rem;
  line-height: 1.8;
}

.stack-section {
  margin-bottom: 2rem;
  padding-bottom: 2rem;
}

.stack-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
}

.stack-item {
  background: rgba(59, 130, 246, 0.1);
  color: #93c5fd;
  padding: 8px 16px;
  border-radius: 6px;
  border: 1px solid rgba(96, 165, 250, 0.2);
  font-size: 0.95rem;
}

.github-section {
  padding-top: 1rem;
}

.github-button {
  background: #3b82f6;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
}

.github-button:hover {
  background: #2563eb;
}

@keyframes pulse {
  0%, 100% {
    opacity: 0.5;
  }
  50% {
    opacity: 0.8;
  }
}

.animate-fade-in {
  animation: fadeIn 0.8s ease-out forwards;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@media (max-width: 768px) {
  .info-container {
    padding: 1rem;
  }

  .main-title {
    font-size: 2rem;
  }

  .info-card {
    padding: 1.5rem;
  }
}
</style>
