import { defineStore } from 'pinia'
import { backAPI } from './backAPI'


export const userEventStore = defineStore('events', {
    state: () => ({
        events: [],
        loading: false,
        error: null
    }),

    actions: {
        async fetchEvents(uid) {
            this.loading = true
            try {
                this.events = await backAPI.getEvents(uid)
            } catch (error) {
                this.error = error
            } finally {
                this.loading = false
            }
        },
        async addEvent(event) {
            try {
                const newEvent = await backAPI.addEvent(event)
                this.events.push(newEvent.data)
            } catch (error) {
                this.error = error.message
                throw error
            }
        },
        getEventsByDate(day, month, year) {
            return this.events.filter(event => 
                event.day === day && 
                event.month === month && 
                event.year === year
            )
        }
    }
})
