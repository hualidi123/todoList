<template>
  <div>
    <div>
      <a-tag :color="color">
        {{ content }}
      </a-tag>
    </div>
  </div>
</template>

<script>
export default {
  props: ['color', 'content'],
}
</script>