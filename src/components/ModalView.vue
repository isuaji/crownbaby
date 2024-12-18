<template>
  <div class="modal-overlay animate-fade-in" @click.self="$emit('close')">
    <div class="modal-container animate-scale-up">
      <div class="modal-content">
        <div class="modal-header">
          <div class="modal-title-wrapper">
            <div class="modal-icon">
              <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                <rect x="3" y="4" width="18" height="18" rx="2" stroke-width="2"/>
                <path d="M16 2v4M8 2v4M3 10h18" stroke-width="2"/>
              </svg>
            </div>
            <h3 class="modal-title">Добавьте событие</h3>
          </div>
        </div>

        <form class="modal-form">
          <div class="input-group">
            <label for="event-title">Название</label>
            <input
              v-model="eventTitle" 
              type="text" 
              id="event-title"
              class="modal-input" 
              :class="{ 'input-error': isTitleEmpty }"
              placeholder="Введите название"
            >
            <span v-if="isTitleEmpty" class="error-message">
              {{ error }}
            </span>
          </div>
          <div class="input-group">
            <label for="event-desc">Описание</label>
            <textarea
              v-model="eventDescription"
              id="event-desc"
              class="modal-textarea"
              :class="{ 'input-error': isDescriptionEmpty }" 
              placeholder="Добавьте описание"
            ></textarea>
            <span v-if="isDescriptionEmpty" class="error-message">
              {{ error }}
            </span>
          </div>
        </form>
        <div class="modal-footer">
          <button class="cancel-btn" @click="$emit('close')">Отмена</button>
          <button class="submit-btn" @click="ifNotEmpty()">Добавить</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { useStore } from '@/pinia'
export default {
  props: {
    day: {
      type: Number,
      required: true
    },
    month: {
      type: Number,
      required: true
    },
    year: {
      type: Number,
      required: true
    }
  },
  name: 'ModalView',
  emits: ['close', 'addevent'],
  
  data() {
    return {
      eventTitle: '',
      eventDescription: '',
      error: '',
      isTitleEmpty: false,
      isDescriptionEmpty: false,
      uid: null
    }
  },

  methods: {
    addEvent() {
      const store = useStore()
      this.uid = store.uid
      const eventData = {
        uid: store.uid,
        title: this.eventTitle,
        description: this.eventDescription,
        day: this.day,
        month: this.month,
        year: this.year
      }
      this.$emit('addevent', eventData)
      this.$emit('close')
    },
    ifNotEmpty() {
      this.isTitleEmpty = false
      this.isDescriptionEmpty = false

      if (this.eventTitle.length < 2) {
        this.error = 'Название события не должно быть таким маленьким'
        this.isTitleEmpty = true
        return
      }
      
      if (this.eventDescription.length < 2) {
        this.error = 'Описание события не должно быть таким маленьким'
        this.isDescriptionEmpty = true
        return
      }
      
      this.addEvent()
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
  backdrop-filter: blur(8px);
}

.modal-container {
  background: linear-gradient(145deg, #111827, #1f2937);
  border-radius: 20px;
  width: 90%;
  max-width: 460px;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.1);
  margin: 0 auto;
}

.modal-content {
  padding: 1.5rem;
  width: 100%;
  box-sizing: border-box;
  animation: slideUp 0.4s ease-out forwards;
}

.modal-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
}

.modal-title-wrapper {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.modal-icon {
  color: #60a5fa;
  display: flex;
  align-items: center;
  transform: scale(1.2);
}

.modal-title {
  color: #fff;
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: -0.025em;
  background: linear-gradient(135deg, #ffffff 0%, #93c5fd 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.close-btn {
  background: none;
  border: none;
  color: #64748b;
  padding: 0.75rem;
  cursor: pointer;
  transition: color 0.2s;
  display: flex;
  align-items: center;
  border-radius: 50%;
  margin-right: -0.5rem;
}

.close-btn:hover {
  color: #94a3b8;
  background: rgba(255, 255, 255, 0.1);
}

.modal-form {
  margin-bottom: 1rem;
}

.input-group {
  margin-bottom: 1rem;
}

.input-group label {
  display: block;
  color: #94a3b8;
  margin-bottom: 0.375rem;
  font-size: 0.95rem;
  font-weight: 500;
}

.modal-input,
.modal-textarea {
  width: 100%;
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 10px;
  padding: 0.75rem;
  color: #fff;
  font-size: 1rem;
  transition: all 0.2s ease;
  font-family: 'Inter', sans-serif;
  box-sizing: border-box;
}

.modal-textarea {
  min-height: 100px;
  resize: vertical;
}

.modal-input::placeholder,
.modal-textarea::placeholder {
  color: #64748b;
}

.modal-input:focus,
.modal-textarea:focus {
  outline: none;
  border-color: #3b82f6;
  background: rgba(15, 23, 42, 0.8);
  box-shadow: 0 0 0 1px rgba(59, 130, 246, 0.5);
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  gap: 0.75rem;
  margin-top: 1.5rem;
}

.cancel-btn,
.submit-btn {
  padding: 0.75rem 1.25rem;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s ease;
}

.cancel-btn {
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: #94a3b8;
}

.cancel-btn:hover {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

.submit-btn {
  background: linear-gradient(135deg, #3b82f6, #2563eb);
  border: none;
  color: #fff;
}

.submit-btn:hover {
  background: linear-gradient(135deg, #2563eb, #1d4ed8);
  transform: translateY(-1px);
}

.submit-btn:active {
  transform: translateY(0);
}

@media (max-width: 768px) {
  .modal-container {
    width: 95%;
  }
  
  .modal-content {
    padding: 1.25rem;
  }

  .modal-title {
    font-size: 1.75rem;
  }

  .modal-icon {
    transform: scale(1.1);
  }
}

.error-message {
  color: #ef4444;
  font-size: 0.875rem;
  margin-top: 0.5rem;
  display: block;
}

.input-error {
  border-color: #ef4444;
  animation: shake 0.5s cubic-bezier(.36,.07,.19,.97) both;
}

@keyframes shake {
  10%, 90% {
    transform: translateX(-1px);
  }
  20%, 80% {
    transform: translateX(2px);
  }
  30%, 50%, 70% {
    transform: translateX(-4px);
  }
  40%, 60% {
    transform: translateX(4px);
  }
}

.animate-fade-in {
  animation: fadeIn 0.15s ease-out forwards;
}

.animate-scale-up {
  animation: scaleUp 0.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    backdrop-filter: blur(0px);
  }
  to {
    opacity: 1;
    backdrop-filter: blur(8px);
  }
}

@keyframes scaleUp {
  from {
    transform: scale(0.95) translateY(10px);
    opacity: 0;
  }
  to {
    transform: scale(1) translateY(0);
    opacity: 1;
  }
}

.modal-content {
  animation: slideUp 0.4s ease-out forwards;
}

@keyframes slideUp {
  from {
    transform: translateY(10px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}
.submit-btn, .cancel-btn {
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

.submit-btn:hover, .cancel-btn:hover {
  transform: translateY(-2px);
}

.submit-btn:active, .cancel-btn:active {
  transform: translateY(0);
}

.modal-input:focus,
.modal-textarea:focus {
  transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  transform: translateY(-1px);
}

.input-error {
  animation: shake 0.4s cubic-bezier(.36,.07,.19,.97) both;
}

@keyframes shake {
  10%, 90% {
    transform: translateX(-1px);
  }
  20%, 80% {
    transform: translateX(2px);
  }
  30%, 50%, 70% {
    transform: translateX(-2px);
  }
  40%, 60% {
    transform: translateX(2px);
  }
}
</style>

