import { defineStore } from 'pinia'
import { v4 as uidv4 } from 'uuid'

export const useStore = defineStore('user', {
    state: () => ({
        uid: null
    }),
    actions: {
        createUid() {
            if (!this.uid) {
                this.uid = uidv4()
            }
            return this.uid
        }
    },
    persist: true
})
