<script>
import { useStore } from '@/pinia'
import axios from 'axios'
import { backAPI } from '@/backAPI'
export default {
  data() {
    return {
      href: ''
    }
  },
  methods: {
    async goToCalendar() {
      const store = useStore()
      store.createUid()
      this.$router.push(`/calendar/${store.uid}`);
      try {
        await backAPI.addUser(store.uid)
      } catch (error) {
      }
    }
  }
}
</script>

<template>
  <div class="welcome-container">
    <div class="static-background">
      <div class="moving-gradient"></div>
    </div>
    <div class="content-wrapper">
      <div class="hero-section">
        <h1 class="title">
          <span class="title-text animate-float">Планируйте время</span>
          <div class="highlight-wrapper">
            <span class="highlight animate-gradient">эффективно</span>
          </div>
        </h1>
        <p class="description animate-fade-in">Простой и удобный календарь для ваших задач</p>
        <button class="cta-button animate-pop-in" @click="goToCalendar()">
          <span class="button-text">Перейти к календарю</span>
          <span class="button-icon">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none">
              <path d="M4 12H20M20 12L14 6M20 12L14 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
            </svg>
          </span>
          <div class="button-glow"></div>
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
  animation: pulseBackground 10s ease-in-out infinite;
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
  text-shadow: 0 0 80px rgba(96, 165, 250, 0.2);
  transition: text-shadow 0.3s ease;
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
  filter: drop-shadow(0 0 30px rgba(96, 165, 250, 0.4));
  transition: all 0.3s ease;
  animation: gradientShift 3s ease-in-out infinite;
}

.highlight:hover {
  filter: drop-shadow(0 0 40px rgba(96, 165, 250, 0.6));
}

.description {
  font-size: 1.5rem;
  color: #a3a3a3;
  margin-bottom: 3rem;
  max-width: 600px;
  line-height: 1.6;
  font-weight: 400;
  letter-spacing: -0.01em;
  opacity: 0;
  animation: fadeIn 1s ease-out 0.6s forwards;
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

.moving-gradient {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(
    circle at center,
    rgba(96, 165, 250, 0.1) 0%,
    rgba(59, 130, 246, 0.05) 25%,
    transparent 50%
  );
  animation: rotate 30s linear infinite, pulse 10s ease-in-out infinite;
}

.animate-slide-down {
  animation: slideDown 0.8s ease-out forwards;
  opacity: 0;
}

.animate-fade-in {
  animation: fadeIn 1s ease-out 0.4s forwards;
  opacity: 0;
}

.animate-pop-in {
  animation: popIn 0.6s cubic-bezier(0.16, 1, 0.3, 1) 0.8s forwards;
  opacity: 0;
  transform: scale(0.8);
}

.animate-gradient {
  background-size: 200% 200%;
  animation: gradientFlow 3s ease infinite;
}

.button-glow {
  position: absolute;
  inset: -2px;
  background: linear-gradient(135deg, #60a5fa, #3b82f6);
  border-radius: 14px;
  z-index: -1;
  opacity: 0;
  transition: opacity 0.3s ease;
  filter: blur(8px);
}

.cta-button:hover .button-glow {
  opacity: 0.6;
}

.highlight::before {
  display: none;
}

@keyframes rotate {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

@keyframes slideDown {
  0% {
    transform: translateY(-30px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(10px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes popIn {
  0% {
    opacity: 0;
    transform: scale(0.8);
  }
  100% {
    opacity: 1;
    transform: scale(1);
  }
}

@keyframes gradientFlow {
  0% {
    background-position: 0% 50%;
  }
  50% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0% 50%;
  }
}

@keyframes pulse {
  0%, 100% {
    transform: scale(1) rotate(0deg);
  }
  50% {
    transform: scale(1.1) rotate(180deg);
  }
}

@keyframes pulseBackground {
  0%, 100% {
    opacity: 0.5;
  }
  50% {
    opacity: 0.7;
  }
}

.animate-float {
  animation: float 4s ease-in-out infinite;
}

.animate-float-slow {
  background: linear-gradient(120deg, #60a5fa, #93c5fd);
  background-size: 200% 200%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.title-text {
  display: block;
  animation: slideDown 0.8s ease-out forwards;
}

@keyframes gradientShift {
  0% {
    background-position: 0% 50%;
    filter: drop-shadow(0 0 30px rgba(96, 165, 250, 0.4));
  }
  50% {
    background-position: 100% 50%;
    filter: drop-shadow(0 0 40px rgba(96, 165, 250, 0.6));
  }
  100% {
    background-position: 0% 50%;
    filter: drop-shadow(0 0 30px rgba(96, 165, 250, 0.4));
  }
}

.preview-image {
  flex: 1;
  max-width: 500px;
  padding: 2rem;
  position: relative;
}

.calendar-preview {
  width: 100%;
  height: auto;
  border: 2px solid transparent;
  border-radius: 20px;
  background: linear-gradient(#1E293B, #1E293B) padding-box,
              linear-gradient(135deg, #60A5FA, #3B82F6, #2563EB) border-box;
  filter: drop-shadow(0 8px 32px rgba(96, 165, 250, 0.2));
  transition: all 0.3s ease;
}

.calendar-preview:hover {
  filter: drop-shadow(0 12px 40px rgba(96, 165, 250, 0.3));
  transform: translateY(-8px);
  border-image: linear-gradient(135deg, #93C5FD, #60A5FA, #3B82F6) 1;
}
</style>