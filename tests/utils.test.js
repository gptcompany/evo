/**
 * Test file for utility functions
 */
import { describe, it, expect } from 'vitest'

// Simple utility functions to test
function sum(numbers) {
  return numbers.reduce((acc, num) => acc + num, 0)
}

function isEven(num) {
  return num % 2 === 0
}

function capitalize(str) {
  if (!str) return str
  return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase()
}

describe('Utility Functions', () => {
  describe('sum', () => {
    it('should return 0 for empty array', () => {
      expect(sum([])).toBe(0)
    })

    it('should sum positive numbers', () => {
      expect(sum([1, 2, 3, 4, 5])).toBe(15)
    })

    it('should handle negative numbers', () => {
      expect(sum([-1, -2, 3])).toBe(0)
    })
  })

  describe('isEven', () => {
    it('should return true for even numbers', () => {
      expect(isEven(2)).toBe(true)
      expect(isEven(0)).toBe(true)
      expect(isEven(-4)).toBe(true)
    })

    it('should return false for odd numbers', () => {
      expect(isEven(1)).toBe(false)
      expect(isEven(3)).toBe(false)
      expect(isEven(-1)).toBe(false)
    })
  })

  describe('capitalize', () => {
    it('should capitalize first letter', () => {
      expect(capitalize('hello')).toBe('Hello')
      expect(capitalize('WORLD')).toBe('World')
    })

    it('should handle empty string', () => {
      expect(capitalize('')).toBe('')
    })

    it('should handle null/undefined', () => {
      expect(capitalize(null)).toBe(null)
      expect(capitalize(undefined)).toBe(undefined)
    })
  })
})