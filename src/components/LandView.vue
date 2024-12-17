<script>
export default {
  data() {
    return {
      href: ''
    }
  },
  methods: {
    goToCalendar() {
      this.$router.push('/calendar');
    }
  }
}
</script>

<template>
  <div class="welcome-container">
    <div class="static-background"></div>
    <div class="content-wrapper">
      <div class="hero-section">
        <h1 class="title">
          Планируйте время
          <div class="highlight-wrapper">
            <span class="highlight">эффективно</span>
          </div>
        </h1>
        <p class="description">Простой и удобный календарь для ваших задач</p>
        <button class="cta-button" @click="goToCalendar()">
          <span class="button-text">Перейти к календарю</span>
          <span class="button-icon">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M4 12H20M20 12L14 6M20 12L14 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </span>
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.welcome-container {
  min-height: 100vh;
  display: grid;
  place-items: center;
  background-color: #000000;
  overflow: hidden;
  font-family: 'Inter', sans-serif;
  padding-bottom: 10vh;
  position: relative;
}

.static-background {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    45deg,
    #000000 0%,
    #0f172a 25%,
    #1e293b 50%,
    #0f172a 75%,
    #000000 100%
  );
  z-index: 0;
  opacity: 0.5;
}

.content-wrapper {
  position: relative;
  width: 100%;
  max-width: 1200px;
  padding: 2rem;
  z-index: 1;
}

.hero-section {
  position: relative;
  z-index: 1;
}

.title {
  font-size: 5rem;
  font-weight: 900;
  line-height: 1.1;
  color: #ffffff;
  margin-bottom: 1.5rem;
  max-width: 800px;
  text-shadow: 0 0 80px rgba(96, 165, 250, 0.1);
}

.highlight-wrapper {
  position: relative;
  display: inline-block;
  margin-top: 0.5rem;
}

.highlight {
  position: relative;
  font-weight: 900;
  background: linear-gradient(120deg, #60a5fa, #93c5fd);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  z-index: 1;
  filter: drop-shadow(0 0 30px rgba(96, 165, 250, 0.3));
}

.description {
  font-size: 1.5rem;
  color: #a3a3a3;
  margin-bottom: 3rem;
  max-width: 600px;
  line-height: 1.6;
  font-weight: 400;
  letter-spacing: -0.01em;
}

.cta-button {
  position: relative;
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.25rem;
  font-weight: 600;
  color: #fff;
  background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
  border: none;
  padding: 1rem 2rem;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 4px 20px rgba(96, 165, 250, 0.2);
}

.button-text {
  z-index: 1;
}

.button-icon {
  display: flex;
  align-items: center;
  transition: transform 0.3s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 25px rgba(59, 130, 246, 0.25);
  background: linear-gradient(135deg, #2563eb 0%, #1d4ed8 100%);
}

.cta-button:hover .button-icon {
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .title {
    font-size: 3rem;
    letter-spacing: -0.03em;
  }

  .description {
    font-size: 1.1rem;
  }

  .cta-button {
    font-size: 1.1rem;
    padding: 0.875rem 2rem;
  }
}
</style>