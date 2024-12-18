import axios from 'axios'

const API_URL = 'http://localhost:5000'

export const backAPI = {
    async getEvents(uid) {
        try {
            const response = await axios.get(`${API_URL}/api/users/${uid}`)
            return response.data
        } catch (error) {
            console.error('Ошибка при получении событий:', error)
            throw error
        }
    },

    async addEvent(eventData) {
        try {
            console.log('Отправляемые данные:', eventData)
            const payload = {
                eventTitle: eventData.title,
                eventDesc: eventData.description,
                eventDateTime: eventData.eventDateTime || new Date().toISOString(),
                eventDay: eventData.day,
                eventMonth: eventData.month,
                eventYear: eventData.year
            }
            console.log('Подготовленные данные для отправки:', payload)
            
            const response = await axios.post(`${API_URL}/events/${eventData.uid}`, payload)
            return response.data
        } catch (error) {
            console.error('Ошибка при добавлении события:', error.response?.data || error)
            throw error
        }
    }
}