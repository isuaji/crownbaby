import { defineStore } from 'pinia'
import { backAPI } from './backAPI'


export const userEventStore = defineStore('events', {
    state: () => ({
        events: [],
        loading: false,
        error: null
    }),

    actions: {
        async addUser(uid) {
            await backAPI.addUser(uid)
        },


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
        async addEvent(eventData) {
            try {
                const response = await backAPI.addEvent(eventData)
                return response
            } catch (error) {
                throw error
            }
        },
        getEventsByDate(day, month, year) {
            return this.events.filter(event => 
                event.day === day && 
                event.month === month && 
                event.year === year
            )
        },
        async updateEvent(eventData) {
            await backAPI.updateEvent(eventData)
        }
    }
})
