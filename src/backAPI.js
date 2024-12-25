import axios from 'axios'

const API_URL = 'http://localhost:5000'

export const backAPI = {
    async addUser(uuid) {
        try {
            const response = await axios.post(`${API_URL}/calendar/${uuid}`, {uuid: uuid})
            return response.data
        } catch (error) {
            throw error
        }
    },

    async getEvents(uuid) {
        try {
            const response = await axios.get(`${API_URL}/api/users/${uuid}`)
            return response.data
        } catch (error) {
            throw error
        }
    },

    async addEvent(eventData) {
        try {
            const payload = {
                eventTime: eventData.eventTime,
                eventTitle: eventData.eventTitle,
                eventDesc: eventData.eventDesc,
                eventDateTime: eventData.eventDateTime || new Date().toISOString(),
                eventDay: eventData.eventDay,
                eventMonth: eventData.eventMonth,
                eventYear: eventData.eventYear
            }        
            const response = await axios.post(`${API_URL}/events/${eventData.uid}`, payload)
            window.location.reload();
            return response.data
        } catch (error) {
            throw error
        }
    },

    async deleteUserEvent(uuid, eventId) {
        try {
            const response = await axios.delete(`${API_URL}/events/delete/${uuid}/${eventId}`)
            window.location.reload();
            return response.data 
        } catch (error) {
            throw error
        }
    },

    async updateEvent(eventData) {
        try {
            const response = await axios.put(`${API_URL}/events/update/${eventData.id}/${eventData.uuid}`, {
                eventTitle: eventData.eventTitle,
                eventDesc: eventData.eventDesc,
                eventTime: eventData.eventTime
            })
            window.location.reload();
            return response.data
        } catch (error) {
            throw error
        }
    }
}