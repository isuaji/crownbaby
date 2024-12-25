<template>
  <div class="events-container">
    <h2 class="events-title">Мои события</h2>
    <div class="events-list">
      <div class="event-card" v-for="event in events" :key="event.id">
        <div class="event-header">
          <h3 class="event-title">{{ event.title }}</h3>
          <div class="event-datetime">
            <span class="event-date">{{ formatDate(event.day, event.month, event.year) }}</span>
            <span class="event-time">{{ event.time }}</span>
          </div>
        </div>
        <div class="event-content">
          <p class="event-description">{{ event.desc }}</p>
        </div>
        <div class="event-actions">
          <button class="btn-edit" @click="editEvent(event)">Редактировать</button>
          <button class="btn-delete" @click="deleteUserEvent(event)">Удалить</button>
        </div>
      </div>
    </div>
    <ModalEditView 
      v-if="showEditModal"
      :event="{
        ...selectedEvent,
        uuid: uuid
      }"
      @close="closeEditModal"
      @save="handleSaveEvent"
    />
  </div>
</template>

<script>
import { backAPI } from '@/backAPI'
import ModalEditView from './ModalEditView.vue'

export default {
  name: 'EventsList',
  components: {
    ModalEditView
  },
  data() {
    return {
      events: [],
      uuid: null,
      showEditModal: false,
      selectedEvent: null
    }
  },
  async created() {
    const uuid = this.$route.params.uid
    this.uuid = uuid
    try {
      const data = await backAPI.getEvents(uuid)
      this.events = data.map(el => ({
        id: el.id,
        title: el.eventTitle,
        desc: el.eventDesc,
        day: el.eventDay,
        month: el.eventMonth,
        year: el.eventYear,
        time: el.eventTime
      }))
    } catch (error) { }
  },
  methods: {
    formatDate(day, month, year) {
      return `${day.toString().padStart(2, '0')}.${month.toString().padStart(2, '0')}.${year}`
    },
    editEvent(event) {
      this.selectedEvent = {
        ...event,
        uuid: this.uuid
      }
      this.showEditModal = true
    },
    closeEditModal() {
      this.showEditModal = false
      this.selectedEvent = null
    },
    async handleSaveEvent(updatedEvent) {
      try {
        await backAPI.updateEvent(updatedEvent)
        const data = await backAPI.getEvents(this.uuid)
        this.events = data.map(el => ({
          id: el.id,
          title: el.eventTitle,
          desc: el.eventDesc,
          day: el.eventDay,
          month: el.eventMonth,
          year: el.eventYear,
          time: el.eventTime
        }))
      } catch (error) {
        console.error('Ошибка при обновлении события:', error)
      }
    },
    async deleteUserEvent(event) {
      if (confirm('Вы уверены, что хотите удалить это событие?')) {
        try {
          await backAPI.deleteUserEvent(event.id, this.uuid)
          console.log('Событие успешно удалено')
        } catch (error) {
          console.error('Ошибка при удалении события:', error)
        }
      }
    }
  }
}
</script>

<style scoped>
.events-container {
  background: transparent;
  border: none;
  height: 100%;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  min-width: 350px;
  width: 400px;
}
.events-title {
  font-size: 1.2rem;
  color: #fff;
  padding: 0.75rem;
  text-align: center;
  font-weight: 600;
  background: rgba(15, 23, 42, 0.4);
  border-radius: 8px;
  margin-bottom: 1rem;
  flex-shrink: 0;
}
.events-list {
  flex: 1;
  overflow-y: auto;
  padding-right: 0.5rem;
  min-height: 0;
  max-height: 600px;
}
.event-card {
  background: rgba(15, 23, 42, 0.4);
  border: 1px solid rgba(96, 165, 250, 0.1);
  border-radius: 6px;
  padding: 0.5rem;
  margin-bottom: 0.5rem;
  min-height: 80px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.event-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.15rem;
}
.event-datetime {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.15rem;
}
.event-date, .event-time {
  font-size: 0.75rem;
  color: #94a3b8;
  background: rgba(148, 163, 184, 0.1);
  padding: 0.15rem 0.3rem;
  border-radius: 3px;
}
.event-title {
  font-size: 0.9rem;
  color: #fff;
  font-weight: 500;
  margin: 0;
  flex: 1;
  margin-right: 0.5rem;
}
.event-description {
  font-size: 0.8rem;
  color: #cbd5e1;
  line-height: 1.2;
  margin: 0.15rem 0;
}
.events-list::-webkit-scrollbar { width: 4px; }
.events-list::-webkit-scrollbar-track { background: transparent; }
.events-list::-webkit-scrollbar-thumb {
  background: rgba(96, 165, 250, 0.2);
  border-radius: 2px;
}
.event-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.3rem;
  margin-top: 0.15rem;
  padding-top: 0.15rem;
  border-top: 1px solid rgba(96, 165, 250, 0.1);
}
.btn-edit, .btn-delete {
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-size: 0.75rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border: none;
}
.btn-edit {
   background: rgba(96, 165, 250, 0.1); color: #60a5fa;
}
.btn-delete { 
  background: rgba(239, 68, 68, 0.1); color: #ef4444; 
}
.btn-edit:hover { 
  background: rgba(96, 165, 250, 0.2); 
}
.btn-delete:hover { 
  background: rgba(239, 68, 68, 0.2); 
}
@media (max-width: 1024px) {
  .events-container {
    width: 100%;
    max-width: 500px;
  }
  .events-list {
    max-height: 500px;
  }
}
@media (max-width: 768px) {
  .events-container {
    width: 100%;
    min-width: unset;
  }
  .events-list {
    max-height: 400px;
  }
}
</style>
