<template>
  <div class="calendar-container animate-fade-in">
    <div class="static-background">
      <div class="moving-gradient"></div>
    </div>
    
    <div class="calendar-header">
      <div class="month-navigation">
        <button class="nav-btn" @click="previousMonth">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M15 18l-6-6 6-6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
        <h2 class="month-title">
          <transition name="slide-fade" mode="out-in">
            <span :key="formattedMonthYear" class="month-text">{{ formattedMonthYear }}</span>
          </transition>
        </h2>
        <button class="nav-btn" @click="nextMonth">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor">
            <path d="M9 18l6-6-6-6" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </button>
      </div>
    </div>

    <div class="calendar-wrapper">
      <transition name="fade-transform" mode="out-in">
        <div class="calendar-grid" :key="currentDate.getMonth()">
          <div v-for="day in weekDays" :key="day" class="weekday-header">
            {{ day }}
          </div>

          <button
            @click="openModal(day)"
            v-for="day in allDays" 
            :key="day.date" 
            :class="[
              'calendar-day',
              { 'prev-month': day.isPrevMonth },
              { 'next-month': day.isNextMonth }
            ]"
          >
            {{ day.dayNumber }}
          </button>
        </div>
      </transition>
    </div>

    <ModalView 
      v-if="showModal" 
      @close="closeModal"
      :day="selectedDay"
      :month="selectedMonth"
      :year="selectedYear"
      @addevent="handleAddEvent"
    />
  </div>
</template>

<script>
import ModalView from './ModalView.vue'
import { useStore } from '@/pinia'

export default {
    components: { ModalView },
  data() {
    return {
      currentDate: new Date(),
      weekDays: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
      showModal: false,
      selectedDay: null,
      selectedMonth: null,
      selectedYear: null,
      uid: null
    }
  },
  userKey() {
    const store = useStore()
      store.createUid()
      console.log(store.uid)
  },

  computed: {
    formattedMonthYear() {
      const month = this.currentDate.toLocaleString('ru', { month: 'long' })
      const year = this.currentDate.getFullYear()
      return month.charAt(0).toUpperCase() + month.slice(1) + ' ' + year
    },

    allDays() {
      const year = this.currentDate.getFullYear()
      const month = this.currentDate.getMonth()
      
      const firstDayOfMonth = new Date(year, month, 1)
      const lastDayOfMonth = new Date(year, month + 1, 0)
      
      let firstDayWeekday = firstDayOfMonth.getDay() || 7
      firstDayWeekday--
      
      const daysArray = []

      const prevMonth = new Date(year, month, 0)
      const prevMonthDays = prevMonth.getDate()
      
      for (let i = firstDayWeekday - 1; i >= 0; i--) {
        daysArray.push({
          date: new Date(year, month - 1, prevMonthDays - i),
          dayNumber: prevMonthDays - i,
          isPrevMonth: true
        })
      }

      for (let i = 1; i <= lastDayOfMonth.getDate(); i++) {
        daysArray.push({
          date: new Date(year, month, i),
          dayNumber: i,
          isCurrentMonth: true
        })
      }

      const remainingDays = 42 - daysArray.length
      for (let i = 1; i <= remainingDays; i++) {
        daysArray.push({
          date: new Date(year, month + 1, i),
          dayNumber: i,
          isNextMonth: true
        })
      }

      return daysArray
    },
    dateEvent() {
        return {
            desc: '',
        }
    }
  },

  methods: {
    previousMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() - 1
      )
    },

    nextMonth() {
      this.currentDate = new Date(
        this.currentDate.getFullYear(),
        this.currentDate.getMonth() + 1
      )
    },

    openModal(day) {
      this.selectedDay = day.dayNumber
      this.selectedMonth = day.date.getMonth() + 1
      this.selectedYear = day.date.getFullYear()
      this.showModal = true
    },
    
    closeModal() {
      this.showModal = false
    },

    handleAddEvent(eventData) {
      const uuid = useStore()
      this.uid = uuid.uid
      console.log(eventData)
    }
  }
}
</script>

<style scoped>
:root {
  overflow: hidden;
}

.calendar-container {
  min-height: 100vh;
  padding: 2rem;
  background-color: #000000;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: 'Inter', sans-serif;
  overflow: hidden;
  max-width: 100vw;
  box-sizing: border-box;
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
  opacity: 0.5;
  z-index: 0;
}

.calendar-header {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 800px;
  margin-bottom: 3rem;
}

.month-navigation {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: rgba(15, 23, 42, 0.6);
  border-radius: 12px;
  margin: 0 1rem;
}

.month-title {
  color: #ffffff;
  font-size: 2.5rem;
  font-weight: 800;
  letter-spacing: -0.04em;
  background: linear-gradient(135deg, #ffffff 0%, #93c5fd 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  padding: 0 1rem;
}

.nav-btn {
  background: rgba(96, 165, 250, 0.15);
  border: none;
  width: 40px;
  height: 40px;
  border-radius: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #60a5fa;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  backdrop-filter: blur(5px);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.nav-btn:hover {
  background: rgba(96, 165, 250, 0.25);
  color: #93c5fd;
  transform: translateY(-2px) scale(1.05);
  box-shadow: 0 4px 12px rgba(96, 165, 250, 0.3);
}

.nav-btn:active {
  transform: translateY(0) scale(0.95);
}

.calendar-wrapper {
  width: 100%;
  max-width: 800px;
  position: relative;
  overflow: hidden;
}

.fade-transform-enter-active,
.fade-transform-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.fade-transform-enter-from {
  opacity: 0;
  transform: scale(0.95) translateY(10px);
}

.fade-transform-leave-to {
  opacity: 0;
  transform: scale(0.95) translateY(-10px);
}

.calendar-grid {
  position: relative;
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 1px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 16px;
  overflow: hidden;
  width: 100%;
  backdrop-filter: blur(10px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  will-change: transform, opacity;
  max-width: 100%;
  box-sizing: border-box;
}

.weekday-header {
  background: rgba(15, 23, 42, 0.9);
  padding: 1.2rem;
  text-align: center;
  font-weight: 700;
  color: #60a5fa;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  font-size: 0.9rem;
  border-bottom: 2px solid rgba(96, 165, 250, 0.2);
}

.calendar-day {
  background: rgba(15, 23, 42, 0.6);
  border: none;
  padding: 1.5rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  color: #e2e8f0;
  min-height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  font-size: 1.1rem;
  letter-spacing: -0.02em;
  position: relative;
  overflow: hidden;
  backdrop-filter: blur(5px);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.05);
}

.calendar-day::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(255, 255, 255, 0.03);
  opacity: 0;
  transition: opacity 0.2s ease;
}

.calendar-day:hover {
  transform: translateY(-2px);
  background: rgba(37, 99, 235, 0.2);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.calendar-day:hover::before {
  opacity: 1;
}

.calendar-day:active {
  transform: translateY(0);
}

.calendar-day:focus {
  outline: none;
  box-shadow: 0 0 0 2px rgba(96, 165, 250, 0.5);
}

.prev-month,
.next-month {
  opacity: 0.5;
  font-weight: 400;
}

@media (max-width: 768px) {
  .calendar-container {
    padding: 1rem;
  }

  .calendar-day {
    padding: 0.75rem;
  }

  .weekday-header {
    padding: 0.75rem;
  }

  .month-title {
    font-size: 1.75rem;
  }

  .nav-btn {
    width: 36px;
    height: 36px;
  }

  .month-navigation {
    padding: 0.75rem;
  }
}

@media (max-width: 480px) {
  .calendar-container {
    padding: 0.5rem;
  }

  .calendar-day {
    padding: 0.5rem;
  }

  .weekday-header {
    padding: 0.5rem;
  }
}

.animate-fade-in {
  animation: fadeIn 0.8s ease-out forwards;
}

.animate-slide-down {
  animation: slideDown 0.6s ease-out forwards;
}

.animate-scale-in {
  animation: scaleIn 0.8s ease-out forwards;
}

.moving-gradient {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(
    circle at center,
    rgba(96, 165, 250, 0.15) 0%,
    rgba(59, 130, 246, 0.1) 25%,
    transparent 50%
  );
  animation: rotate 30s linear infinite,
             pulse 10s ease-in-out infinite;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes slideDown {
  from {
    transform: translateY(-20px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

@keyframes scaleIn {
  from {
    transform: scale(0.98);
    opacity: 0;
  }
  to {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.stars {
  position: absolute;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(2px 2px at 20px 30px, #eee, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 40px 70px, #fff, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 50px 160px, #ddd, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 90px 40px, #fff, rgba(0,0,0,0)),
                    radial-gradient(2px 2px at 130px 80px, #fff, rgba(0,0,0,0));
  background-repeat: repeat;
  background-size: 200px 200px;
  animation: twinkle 4s ease-in-out infinite;
  opacity: 0.3;
}

.month-text {
  display: inline-block;
  min-width: 200px;
  text-align: center;
}

.slide-fade-enter-active,
.slide-fade-leave-active {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.slide-fade-enter-from {
  opacity: 0;
  transform: translateX(20px);
}

.slide-fade-leave-to {
  opacity: 0;
  transform: translateX(-20px);
}
.calendar-day {
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
}

.calendar-day:hover {
  transform: translateY(-2px);
  background: rgba(37, 99, 235, 0.2);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.2);
}

.calendar-day:active {
  transform: translateY(0);
}

</style>
