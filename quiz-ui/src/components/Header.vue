 <template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <RouterLink to="/" class="nav-brand"><i class="fa fa-home"></i></RouterLink>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
        aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <RouterLink to="/about" class="nav-link">About</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink to="/loginPage" class="nav-link">Login</RouterLink>
          </li>
        </ul>
      </div>
    </nav>
  </header>
</template>
<script>
export default {
  name: 'Header',
}
</script>